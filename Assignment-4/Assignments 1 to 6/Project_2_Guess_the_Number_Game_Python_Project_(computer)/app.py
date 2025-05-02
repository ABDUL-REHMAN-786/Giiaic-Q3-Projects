import streamlit as st
import random
import time

# Function to reset the game
def reset_game():
    difficulty_settings = {
        "Easy (1-50)": (1, 50),
        "Medium (1-100)": (1, 100),
        "Hard (1-200)": (1, 200)
    }
    
    selected_difficulty = st.session_state.get('difficulty', "Medium (1-100)")
    min_val, max_val = difficulty_settings[selected_difficulty]

    st.session_state['random_number'] = random.randint(min_val, max_val)
    st.session_state['attempts'] = 0
    st.session_state['guess_history'] = []
    st.session_state['game_over'] = False
    st.session_state['message'] = f"🎯 Guess a number between {min_val} and {max_val}!"
    st.session_state['turn'] = 0  # Track player turns
    st.session_state['start_time'] = time.time()  # Start time tracking
    st.session_state['ai_guess'] = None  # AI opponent's guess

# Function for AI opponent guessing
def ai_guess_number(min_val, max_val):
    return random.randint(min_val, max_val)

# Initialize session state
if 'random_number' not in st.session_state:
    reset_game()

# Streamlit UI
st.title("🎲 Guess the Number Game")
st.write("Try to guess the number chosen by the computer!")

# Difficulty Selection
if st.session_state['attempts'] == 0:
    difficulty = st.selectbox("Select Difficulty:", ["Easy (1-50)", "Medium (1-100)", "Hard (1-200)"], index=1)
    st.session_state['difficulty'] = difficulty

# Multiplayer Mode
multiplayer = st.checkbox("👥 Enable Multiplayer Mode", value=False)
num_players = 1 if not multiplayer else st.slider("Number of Players:", 1, 4, 2)

# AI Opponent Mode
ai_opponent = st.checkbox("🤖 Enable AI Opponent", value=False)

# User input
user_guess = st.number_input("Enter your guess:", min_value=1, max_value=200, step=1)

# Submit button
if st.button("Check Guess") and not st.session_state['game_over']:
    st.session_state['attempts'] += 1
    st.session_state['guess_history'].append(user_guess)

    correct_number = st.session_state['random_number']
    current_player = (st.session_state['turn'] % num_players) + 1  # Determine player turn

    if user_guess < correct_number:
        st.session_state['message'] = f"🔼 Too low! Player {current_player}, try a higher number."
    elif user_guess > correct_number:
        st.session_state['message'] = f"🔽 Too high! Player {current_player}, try a lower number."
    else:
        end_time = time.time()
        time_taken = round(end_time - st.session_state['start_time'], 2)
        score = max(100 - st.session_state['attempts'] * 5 - time_taken, 0)  # Score calculation
        st.session_state['message'] = f"🎉 Correct! Player {current_player} guessed it in {st.session_state['attempts']} attempts! 🏆 Score: {score}"
        st.session_state['game_over'] = True
        st.balloons()  # Celebrate with balloons!

        # Save to leaderboard
        if 'leaderboard' not in st.session_state:
            st.session_state['leaderboard'] = []
        st.session_state['leaderboard'].append({"player": current_player, "score": score, "attempts": st.session_state['attempts'], "time": time_taken})
        st.session_state['leaderboard'] = sorted(st.session_state['leaderboard'], key=lambda x: (-x['score'], x['attempts'], x['time']))

    # AI Opponent's Turn
    if ai_opponent and not st.session_state['game_over']:
        ai_guess = ai_guess_number(1, 200)
        st.session_state['ai_guess'] = ai_guess
        if ai_guess == correct_number:
            st.session_state['message'] = f"🤖 AI guessed the correct number **{ai_guess}**! AI wins!"
            st.session_state['game_over'] = True

    # Update turn for multiplayer
    st.session_state['turn'] += 1

# Display message
st.success(st.session_state['message'])

# Show AI Opponent's Guess
if ai_opponent and st.session_state['ai_guess']:
    st.write(f"🤖 AI guessed: **{st.session_state['ai_guess']}**")

# Show Guess History
if st.session_state['attempts'] > 0:
    st.write("📜 **Guess History:**", ", ".join(map(str, st.session_state['guess_history'])))

# Show Leaderboard
if 'leaderboard' in st.session_state and st.session_state['leaderboard']:
    st.subheader("🏆 Leaderboard")
    for idx, entry in enumerate(st.session_state['leaderboard']):
        st.write(f"**{idx + 1}. Player {entry['player']}** - Score: {entry['score']} | Attempts: {entry['attempts']} | Time: {entry['time']}s")

# Play sound effects (if game is won)
if st.session_state['game_over']:
    st.audio("https://www.soundjay.com/button/beep-07.wav", format="audio/wav")

# Reset button
if st.button("🔄 Play Again"):
    reset_game()



# # # import streamlit as st
# # # import random
# # # import time
# # # import firebase_admin
# # # from firebase_admin import credentials, db

# # # # Firebase Configuration
# # # if not firebase_admin._apps:
# # #     cred = credentials.Certificate("firebase_config.json")  # 🔥 Add your Firebase key
# # #     firebase_admin.initialize_app(cred, {"databaseURL": "https://guess-number-a2a5f-default-rtdb.firebaseio.com/"})

# # # # Initialize Multiplayer Game Room
# # # def create_game_room():
# # #     room_code = str(random.randint(1000, 9999))  # Generate a 4-digit room code
# # #     db.reference(f"rooms/{room_code}").set({
# # #         "players": {},
# # #         "status": "waiting",
# # #         "number": random.randint(1, 100),
# # #         "history": [],
# # #         "chat": [],
# # #     })
# # #     return room_code

# # # # Join Game Room
# # # def join_game(room_code, player_name):
# # #     room_ref = db.reference(f"rooms/{room_code}")
# # #     if room_ref.get():
# # #         room_ref.child("players").update({player_name: 0})  # 0 = Not guessed yet
# # #         return True
# # #     return False

# # # # Send Chat Message
# # # def send_chat_message(room_code, player_name, message):
# # #     db.reference(f"rooms/{room_code}/chat").push({"player": player_name, "message": message})

# # # # Adaptive AI Guessing (Beginner, Intermediate, Expert)
# # # def ai_guess_number(ai_level, min_val, max_val):
# # #     if ai_level == "Beginner":
# # #         return random.randint(min_val, max_val)
# # #     elif ai_level == "Intermediate":
# # #         return (min_val + max_val) // 2
# # #     else:  # Expert AI (Binary Search)
# # #         return (min_val + max_val) // 2 if random.random() > 0.3 else random.randint(min_val, max_val)

# # # # Streamlit UI
# # # st.title("🌍 Online Multiplayer Guess the Number")

# # # # Lobby Creation or Joining
# # # if "room_code" not in st.session_state:
# # #     st.session_state["room_code"] = None
# # #     st.session_state["player_name"] = None

# # # if not st.session_state["room_code"]:
# # #     option = st.radio("Do you want to create or join a game?", ["Create Game", "Join Game"])
    
# # #     if option == "Create Game":
# # #         if st.button("Create Lobby"):
# # #             room_code = create_game_room()
# # #             st.session_state["room_code"] = room_code
# # #             st.session_state["player_name"] = "Host"
# # #             st.success(f"🎉 Game Room Created! Share this code: `{room_code}`")
    
# # #     elif option == "Join Game":
# # #         room_code = st.text_input("Enter Room Code:")
# # #         player_name = st.text_input("Enter Your Name:")
        
# # #         if st.button("Join Game"):
# # #             if join_game(room_code, player_name):
# # #                 st.session_state["room_code"] = room_code
# # #                 st.session_state["player_name"] = player_name
# # #                 st.success(f"🎉 Joined Room `{room_code}` as `{player_name}`")
# # #             else:
# # #                 st.error("Invalid Room Code! Try Again.")

# # # # Game Logic (If Inside a Room)
# # # if st.session_state["room_code"]:
# # #     room_code = st.session_state["room_code"]
# # #     player_name = st.session_state["player_name"]
# # #     room_ref = db.reference(f"rooms/{room_code}")
# # #     game_data = room_ref.get()

# # #     if game_data and game_data["status"] == "waiting":
# # #         st.write("Waiting for players to join...")

# # #         if st.button("Start Game"):
# # #             room_ref.update({"status": "active"})

# # #     elif game_data and game_data["status"] == "active":
# # #         # Display Chat
# # #         st.subheader("💬 Chat")
# # #         chat_data = room_ref.child("chat").get() or []
# # #         for msg in chat_data:
# # #             st.write(f"**{msg['player']}:** {msg['message']}")
        
# # #         # Send Message
# # #         message = st.text_input("Type a message:")
# # #         if st.button("Send"):
# # #             send_chat_message(room_code, player_name, message)

# # #         # Game Guessing
# # #         user_guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)
# # #         if st.button("Submit Guess"):
# # #             correct_number = game_data["number"]
# # #             if user_guess == correct_number:
# # #                 st.success(f"🎉 {player_name} guessed the correct number!")
# # #                 room_ref.update({"status": "finished"})
# # #             else:
# # #                 room_ref.child("history").push({player_name: user_guess})
# # #                 st.warning("Try Again!")

# # #         # AI Opponent Guess
# # #         ai_level = st.selectbox("Select AI Difficulty", ["Beginner", "Intermediate", "Expert"])
# # #         ai_guess = ai_guess_number(ai_level, 1, 100)
# # #         st.write(f"🤖 AI guessed: **{ai_guess}**")

# # #         if ai_guess == correct_number:
# # #             st.error(f"🤖 AI Wins! The correct number was {correct_number}")
# # #             room_ref.update({"status": "finished"})

# # #     elif game_data and game_data["status"] == "finished":
# # #         st.success("🎉 Game Over!")
# # #         if st.button("Play Again"):
# # #             room_ref.update({"status": "waiting", "number": random.randint(1, 100), "history": [], "chat": []})
# # #             st.session_state["room_code"] = None



# # import random
# # import streamlit as st
# # import firebase_admin
# # from firebase_admin import credentials, db

# # # Initialize Firebase
# # cred = credentials.Certificate("firebase_config.json")
# # firebase_admin.initialize_app(cred, {
# #     "databaseURL": "https://guess-number-a2a5f-default-rtdb.firebaseio.com/"
# # })

# # # Function to create a new game room
# # def create_game_room():
# #     room_code = str(random.randint(1000, 9999))  # Simple room code generator
# #     room_ref = db.reference(f"rooms/{room_code}")
# #     room_ref.set({
# #         "players": {},
# #         "chat": [],
# #         "game_active": True
# #     })
# #     return room_code

# # # Function to join an existing game room
# # def join_game(room_code, player_name):
# #     room_ref = db.reference(f"rooms/{room_code}")
# #     room = room_ref.get()
# #     if room and room.get("game_active"):
# #         players = room.get("players", {})
# #         if player_name not in players:
# #             players[player_name] = {"score": 0}
# #             room_ref.update({"players": players})
# #             return True
# #     return False

# # # Function for AI guess
# # def ai_guess_logic(correct_number):
# #     ai_guess = random.randint(1, 100)  # AI guesses a number between 1 and 100
# #     print(f"AI's guess: {ai_guess}")
    
# #     if ai_guess == correct_number:
# #         return True  # AI guessed correctly
# #     return False

# # # Start the Streamlit app
# # def main():
# #     st.title("🌍 Online Multiplayer Guess the Number")

# #     # Choose between creating or joining a game
# #     choice = st.radio("Do you want to create or join a game?", ["Create Game", "Join Game"])

# #     if choice == "Create Game":
# #         room_code = create_game_room()
# #         st.success(f"Game room created! Room code: {room_code}")
# #         player_name = st.text_input("Enter your player name:")
# #         if player_name:
# #             st.write(f"Waiting for other players to join the game...")
# #             room_ref = db.reference(f"rooms/{room_code}")
# #             while True:
# #                 room = room_ref.get()
# #                 players = room.get("players", {})
# #                 if len(players) > 1:
# #                     st.write("Game has started!")
# #                     break  # Proceed when there are more than one player
# #                 st.time.sleep(2)  # Check every 2 seconds for other players

# #             correct_number = random.randint(1, 100)
# #             st.write("Game started! Guess the number between 1 and 100.")

# #             # Main game loop (you can adjust this)
# #             player_guess = st.number_input("Your guess:", min_value=1, max_value=100)
# #             if player_guess:
# #                 if player_guess == correct_number:
# #                     st.success(f"Congratulations! You guessed the number {correct_number} correctly!")
# #                 else:
# #                     st.error(f"Oops! The correct number was {correct_number}.")

# #             # AI logic to guess the number
# #             ai_correct = ai_guess_logic(correct_number)
# #             if ai_correct:
# #                 st.success("AI guessed the correct number!")
# #             else:
# #                 st.write("AI guessed incorrectly.")

# #     elif choice == "Join Game":
# #         room_code = st.text_input("Enter room code:")
# #         player_name = st.text_input("Enter your player name:")
# #         if room_code and player_name:
# #             if join_game(room_code, player_name):
# #                 st.success(f"Joined room {room_code} as {player_name}")
# #                 st.write("Waiting for the game to start...")

# #                 # Fetch game data from Firebase
# #                 room_ref = db.reference(f"rooms/{room_code}")
# #                 room = room_ref.get()
# #                 correct_number = random.randint(1, 100)
# #                 st.write("Game started! Guess the number between 1 and 100.")

# #                 # Player guess input
# #                 player_guess = st.number_input("Your guess:", min_value=1, max_value=100)
# #                 if player_guess:
# #                     if player_guess == correct_number:
# #                         st.success(f"Congratulations! You guessed the number {correct_number} correctly!")
# #                     else:
# #                         st.error(f"Oops! The correct number was {correct_number}.")

# #                 # AI guess logic
# #                 ai_correct = ai_guess_logic(correct_number)
# #                 if ai_correct:
# #                     st.success("AI guessed the correct number!")
# #                 else:
# #                     st.write("AI guessed incorrectly.")
# #             else:
# #                 st.error("Room code is invalid or game is already full.")
    
# # # Run the app
# # if __name__ == "__main__":
# #     main()





# import random
# import streamlit as st
# import firebase_admin
# from firebase_admin import credentials, db

# # Initialize Firebase (only once)
# if not firebase_admin._apps:
#     cred = credentials.Certificate("firebase_config.json")
#     firebase_admin.initialize_app(cred, {
#         "databaseURL": "https://guess-number-a2a5f-default-rtdb.firebaseio.com/"
#     })
# else:
#     print("Firebase app already initialized.")

# # Function to create a new game room
# def create_game_room():
#     room_code = str(random.randint(1000, 9999))  # Simple room code generator
#     room_ref = db.reference(f"rooms/{room_code}")
#     room_ref.set({
#         "players": {},
#         "chat": [],
#         "game_active": True
#     })
#     return room_code

# # Function to join an existing game room
# def join_game(room_code, player_name):
#     room_ref = db.reference(f"rooms/{room_code}")
#     room = room_ref.get()
#     if room and room.get("game_active"):
#         players = room.get("players", {})
#         if player_name not in players:
#             players[player_name] = {"score": 0}
#             room_ref.update({"players": players})
#             return True
#     return False

# # Function for AI guess
# def ai_guess_logic(correct_number):
#     ai_guess = random.randint(1, 100)  # AI guesses a number between 1 and 100
#     print(f"AI's guess: {ai_guess}")
    
#     if ai_guess == correct_number:
#         return True  # AI guessed correctly
#     return False

# # Start the Streamlit app
# def main():
#     st.title("🌍 Online Multiplayer Guess the Number")

#     # Choose between creating or joining a game
#     choice = st.radio("Do you want to create or join a game?", ["Create Game", "Join Game"])

#     if choice == "Create Game":
#         room_code = create_game_room()
#         st.success(f"Game room created! Room code: {room_code}")
#         player_name = st.text_input("Enter your player name:")
#         if player_name:
#             st.write(f"Waiting for other players to join the game...")
#             room_ref = db.reference(f"rooms/{room_code}")
#             while True:
#                 room = room_ref.get()
#                 players = room.get("players", {})
#                 if len(players) > 1:
#                     st.write("Game has started!")
#                     break  # Proceed when there are more than one player
#                 import time
#                 time.sleep(2)  # Check every 2 seconds for other players

#             correct_number = random.randint(1, 100)
#             st.write("Game started! Guess the number between 1 and 100.")

#             # Main game loop (you can adjust this)
#             player_guess = st.number_input("Your guess:", min_value=1, max_value=100)
#             if player_guess:
#                 if player_guess == correct_number:
#                     st.success(f"Congratulations! You guessed the number {correct_number} correctly!")
#                 else:
#                     st.error(f"Oops! The correct number was {correct_number}.")

#             # AI logic to guess the number
#             ai_correct = ai_guess_logic(correct_number)
#             if ai_correct:
#                 st.success("AI guessed the correct number!")
#             else:
#                 st.write("AI guessed incorrectly.")

#     elif choice == "Join Game":
#         room_code = st.text_input("Enter room code:")
#         player_name = st.text_input("Enter your player name:")
#         if room_code and player_name:
#             if join_game(room_code, player_name):
#                 st.success(f"Joined room {room_code} as {player_name}")
#                 st.write("Waiting for the game to start...")

#                 # Fetch game data from Firebase
#                 room_ref = db.reference(f"rooms/{room_code}")
#                 room = room_ref.get()
#                 correct_number = random.randint(1, 100)
#                 st.write("Game started! Guess the number between 1 and 100.")

#                 # Player guess input
#                 player_guess = st.number_input("Your guess:", min_value=1, max_value=100)
#                 if player_guess:
#                     if player_guess == correct_number:
#                         st.success(f"Congratulations! You guessed the number {correct_number} correctly!")
#                     else:
#                         st.error(f"Oops! The correct number was {correct_number}.")

#                 # AI guess logic
#                 ai_correct = ai_guess_logic(correct_number)
#                 if ai_correct:
#                     st.success("AI guessed the correct number!")
#                 else:
#                     st.write("AI guessed incorrectly.")
#             else:
#                 st.error("Room code is invalid or game is already full.")
    
# # Run the app
# if __name__ == "__main__":
#     main()
