# # Inventory Management System using Streamlit
# # This code provides a simple inventory management system with CRUD operations using Streamlit and SQLAlchemy.
# import streamlit as st
# from datetime import datetime
# from models import Item, PerishableItem, ElectronicItem, Session
# import time
# import random
# import pandas as pd

# st.set_page_config(page_title="Inventory Management System", layout="wide")

# # Global styles for layout and animations
# st.markdown("""
#     <style>
#     .main { max-width: 1200px; padding: 2rem; }
#     .stButton>button {
#         width: 100%;
#         transition: all 0.3s ease;
#     }
#     .stButton>button:hover {
#         transform: scale(1.05);
#     }
#     .title-text {
#         color: #4a4a4a;
#         text-align: center;
#         margin-bottom: 2rem;
#     }
#     .balloon {
#         position: fixed;
#         bottom: 0;
#         font-size: 20px;
#         animation: float 4s ease-in-out infinite;
#     }
#     @keyframes float {
#         0% { transform: translateY(0) rotate(0deg); }
#         50% { transform: translateY(-100px) rotate(10deg); }
#         100% { transform: translateY(-200px) rotate(0deg); opacity: 0; }
#     }
#     .block-container {
#         display: flex;
#         flex-direction: column;
#         min-height: 100vh;
#     }
#     footer {
#         margin-top: auto;
#     }
#     </style>
# """, unsafe_allow_html=True)

# # Session state initialization
# if 'current_page' not in st.session_state:
#     st.session_state.current_page = "Home"
# if 'show_success' not in st.session_state:
#     st.session_state.show_success = False
# if 'success_message' not in st.session_state:
#     st.session_state.success_message = ""
# if 'show_balloons' not in st.session_state:
#     st.session_state.show_balloons = False
# if 'view_mode' not in st.session_state:
#     st.session_state.view_mode = "cards"

# # Header and footer
# def render_header():
#     st.markdown("""
#         <div style="background-color:#f0f2f6;padding:1rem;border-radius:10px;margin-bottom:2rem;">
#             <h2 style="color:#333;text-align:center;">📦 Inventory Management System</h2>
#         </div>
#     """, unsafe_allow_html=True)

# def render_footer():
#     st.markdown("""
#         <hr>
#         <footer>
#             <div style="text-align:center; color: gray; font-size: 0.9rem;">
#                 © 2025 InventoryPro. Built with ❤️ using Streamlit.
#             </div>
#         </footer>
#     """, unsafe_allow_html=True)

# # Animation helpers
# def balloon_animation():
#     st.session_state.show_balloons = True
#     time.sleep(2)
#     st.session_state.show_balloons = False

# def success_animation(message):
#     st.session_state.show_success = True
#     st.session_state.success_message = message
#     balloon_animation()
#     time.sleep(1.5)
#     st.session_state.show_success = False

# # Pages
# def home_page():
#     render_header()
#     st.write("Welcome to the Inventory Management System. Please select an option below.")
    
#     col1, col2, col3, col4 = st.columns(4)
#     with col1:
#         if st.button("➕ Add New Item", key="add_new_item_button"):
#             st.session_state.current_page = "Add Item"
#     with col2:
#         if st.button("✏️ Update Existing Item", key="update_item_button"):
#             st.session_state.current_page = "Update Item"
#     with col3:
#         if st.button("📋 View Inventory", key="view_inventory_button"):
#             st.session_state.current_page = "View Inventory"
#     with col4:
#         if st.button("🗑️ Delete Items", key="delete_items_button"):
#             st.session_state.current_page = "Delete Items"

#     if st.session_state.show_success:
#         st.success(st.session_state.success_message, icon="✅")

#     if st.session_state.show_balloons:
#         for _ in range(10):
#             st.markdown(f"""
#                 <div class="balloon" style="left: {random.randint(10, 90)}%; animation-delay: {random.random()}s;">
#                     {'🎈' if random.random() > 0.5 else '🎉'}
#                 </div>
#             """, unsafe_allow_html=True)

#     render_footer()

# def view_inventory_page():
#     render_header()
#     st.title("📋 Current Inventory")
#     st.button("← Back to Home", on_click=lambda: setattr(st.session_state, 'current_page', 'Home'), key="back_to_home_inventory")

#     col1, col2 = st.columns([1, 4])
#     with col1:
#         st.session_state.view_mode = st.radio(
#             "View Mode", ["Cards", "Table"], horizontal=True,
#             index=0 if st.session_state.view_mode == "cards" else 1,
#             key="view_mode_radio"
#         ).lower()

#     session = Session()
#     items = session.query(Item).all()

#     if not items:
#         st.warning("No items in inventory.")
#         session.close()
#         render_footer()
#         return

#     total_value = sum(item.calculate_total_price() for item in items)
#     st.subheader(f"💰 Total Inventory Value: ${total_value:,.2f}")

#     if st.session_state.view_mode == "cards":
#         for item in items:
#             with st.container():
#                 st.markdown("----")
#                 st.subheader(f"{item.name} (ID: {item.item_id})")
#                 st.write(f"📦 Quantity: {item.quantity}")
#                 st.write(f"💵 Price: ${item.price:.2f}")
#                 if isinstance(item, PerishableItem):
#                     st.write(f"📅 Expiry Date: {item.expiry_date.strftime('%Y-%m-%d')}")
#                 if isinstance(item, ElectronicItem):
#                     st.write(f"🔋 Warranty: {item.warranty_years} years")
#                 st.metric("Total Value", f"${item.calculate_total_price():,.2f}")
#     else:
#         inventory_data = []
#         for item in items:
#             item_dict = {
#                 "ID": item.item_id,
#                 "Name": item.name,
#                 "Type": item.item_type.capitalize(),
#                 "Quantity": item.quantity,
#                 "Price": f"${item.price:.2f}",
#                 "Total Value": f"${item.calculate_total_price():,.2f}"
#             }
#             if isinstance(item, PerishableItem):
#                 item_dict["Expiry Date"] = item.expiry_date.strftime('%Y-%m-%d')
#             elif isinstance(item, ElectronicItem):
#                 item_dict["Warranty"] = f"{item.warranty_years} years"
#             inventory_data.append(item_dict)

#         df = pd.DataFrame(inventory_data)
#         st.dataframe(df, use_container_width=True)

#     session.close()
#     render_footer()

# def delete_items_page():
#     render_header()
#     st.title("🗑️ Delete Items")
#     st.button("← Back to Home", on_click=lambda: setattr(st.session_state, 'current_page', 'Home'), key="back_to_home_delete")

#     session = Session()
#     items = session.query(Item).all()

#     if not items:
#         st.warning("No items to delete.")
#         session.close()
#         render_footer()
#         return

#     st.subheader("Select items to delete:")

#     item_ids_to_delete = []
#     for item in items:
#         item_label = f"{item.name} (ID: {item.item_id})"
#         if st.checkbox(f"❌ {item_label}", key=f"delete_{item.item_id}"):
#             item_ids_to_delete.append(item.item_id)

#     if item_ids_to_delete:
#         if st.button("🚨 Delete Selected Items", key="delete_selected_items_button"):
#             for item_id in item_ids_to_delete:
#                 item = session.query(Item).filter(Item.item_id == item_id).first()
#                 if item:
#                     session.delete(item)
#             session.commit()
#             session.close()
#             success_animation(f"Successfully deleted {len(item_ids_to_delete)} item(s).")
#             st.rerun()
#     else:
#         st.info("No items selected for deletion.")

#     render_footer()

# def update_item_page():
#     render_header()
#     st.title("✏️ Update Existing Item")
#     st.button("← Back to Home", on_click=lambda: setattr(st.session_state, 'current_page', 'Home'), key="back_to_home_update")

#     session = Session()
#     items = session.query(Item).all()
#     if not items:
#         st.warning("No items to update.")
#         session.close()
#         render_footer()
#         return

#     item_options = {f"{item.name} (ID: {item.item_id})": item.item_id for item in items}
#     selected_label = st.selectbox("Select item to update", list(item_options.keys()), key="select_item_to_update")
#     selected_id = item_options[selected_label]
#     item = session.query(Item).filter(Item.item_id == selected_id).first()

#     st.subheader(f"Editing: {item.name} (ID: {item.item_id})")

#     new_name = st.text_input("Item Name", item.name, key="new_item_name")
#     new_quantity = st.number_input("Quantity", min_value=1, value=item.quantity, key="new_item_quantity")
#     new_price = st.number_input("Price", min_value=0.0, format="%.2f", value=float(item.price), key="new_item_price")

#     if isinstance(item, PerishableItem):
#         new_expiry = st.date_input("Expiry Date", item.expiry_date, key="new_item_expiry")
#     elif isinstance(item, ElectronicItem):
#         new_warranty = st.number_input("Warranty (years)", min_value=0, value=item.warranty_years, key="new_item_warranty")

#     if st.button("💾 Save Changes", key="save_changes_button"):
#         item.name = new_name
#         item.quantity = new_quantity
#         item.price = new_price
#         if isinstance(item, PerishableItem):
#             item.expiry_date = new_expiry
#         elif isinstance(item, ElectronicItem):
#             item.warranty_years = new_warranty

#         session.commit()
#         session.close()
#         success_animation(f"Successfully updated '{new_name}'.")
#         st.session_state.current_page = "Home"

#     render_footer()

# def add_item_page():
#     render_header()
#     st.title("➕ Add New Item")
    
#     item_type = st.selectbox("Select Item Type", ["Perishable", "Electronic", "General"], key="add_item_type")

#     new_name = st.text_input("Item Name", key="new_item_name_input")
#     new_quantity = st.number_input("Quantity", min_value=1, key="new_item_quantity_input")
#     new_price = st.number_input("Price", min_value=0.0, format="%.2f", key="new_item_price_input")
    
#     if item_type == "Perishable":
#         new_expiry = st.date_input("Expiry Date", key="new_item_expiry_input")
#         item = PerishableItem(name=new_name, quantity=new_quantity, price=new_price, expiry_date=new_expiry)
#     elif item_type == "Electronic":
#         new_warranty = st.number_input("Warranty (years)", min_value=0, key="new_item_warranty_input")
#         item = ElectronicItem(name=new_name, quantity=new_quantity, price=new_price, warranty_years=new_warranty)
#     else:
#         item = Item(name=new_name, quantity=new_quantity, price=new_price)
    
#     if st.button("Add Item", key="add_item_button"):
#         session = Session()
#         session.add(item)
#         session.commit()
#         session.close()
#         success_animation(f"Item '{new_name}' added successfully.")
#         st.session_state.current_page = "Home"

#     st.button("← Back to Home", on_click=lambda: setattr(st.session_state, 'current_page', 'Home'), key="back_to_home_add")
#     render_footer()

# # App Routing
# if st.session_state.current_page == "Home":
#     home_page()
# elif st.session_state.current_page == "Add Item":
#     add_item_page()
# elif st.session_state.current_page == "Update Item":
#     update_item_page()
# elif st.session_state.current_page == "View Inventory":
#     view_inventory_page()
# elif st.session_state.current_page == "Delete Items":
#     delete_items_page()






import streamlit as st
from datetime import datetime
from models import Item, PerishableItem, ElectronicItem, Session
import time
import random
import pandas as pd

st.set_page_config(page_title="Inventory Management System", layout="wide")

# Global CSS
st.markdown("""
    <style>
    .main { max-width: 1200px; padding: 2rem; }
    .stButton>button {
        width: 100%;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: scale(1.05);
    }
    .balloon-container {
        position: fixed;
        bottom: -100px;
        left: 50%;
        transform: translateX(-50%);
        z-index: 9999;
        pointer-events: none;
    }
    .balloon {
        width: 30px;
        height: 40px;
        background-color: #ff4b4b;
        border-radius: 50% 50% 50% 50%;
        margin: 10px auto;
        animation: rise 4s ease-in-out forwards;
    }
    .balloon::after {
        content: '';
        position: absolute;
        width: 2px;
        height: 20px;
        background: #555;
        top: 40px;
        left: 50%;
        transform: translateX(-50%);
    }
    @keyframes rise {
        0% { transform: translateY(0) translateX(-50%); opacity: 1; }
        100% { transform: translateY(-600px) translateX(-50%); opacity: 0; }
    }
    footer {
        margin-top: auto;
    }
    </style>
""", unsafe_allow_html=True)

# Session State
for key in ['current_page', 'show_success', 'success_message', 'show_balloons', 'view_mode']:
    if key not in st.session_state:
        st.session_state[key] = {
            'current_page': "Home",
            'show_success': False,
            'success_message': "",
            'show_balloons': False,
            'view_mode': "cards"
        }.get(key)

# Header and Footer
def render_header():
    st.markdown("""
        <div style="background-color:#f0f2f6;padding:1rem;border-radius:10px;margin-bottom:2rem;">
            <h2 style="color:#333;text-align:center;">📦 Inventory Management System</h2>
        </div>
    """, unsafe_allow_html=True)

def render_footer():
    st.markdown("""
        <hr>
        <footer>
            <div style="text-align:center; color: gray; font-size: 0.9rem;">
                © 2025 InventoryPro. Built with ❤️ using Streamlit.
            </div>
        </footer>
    """, unsafe_allow_html=True)

# PIP-style balloon animation
def pip_balloon_animation():
    st.markdown(f"""
        <div class="balloon-container">
            {''.join('<div class="balloon" style="background-color:{};"></div>'.format(random.choice(['#ff4b4b','#ff7f50','#ffd700','#87ceeb','#32cd32'])) for _ in range(7))}
        </div>
    """, unsafe_allow_html=True)

# Success handler
def success_animation(message):
    st.session_state.show_success = True
    st.session_state.success_message = message
    st.session_state.show_balloons = True
    pip_balloon_animation()
    time.sleep(1.5)
    st.session_state.show_success = False
    st.session_state.show_balloons = False

# Pages
def home_page():
    render_header()
    st.write("Welcome to the Inventory Management System. Please select an option below.")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button("➕ Add New Item"):
            st.session_state.current_page = "Add Item"
    with col2:
        if st.button("✏️ Update Existing Item"):
            st.session_state.current_page = "Update Item"
    with col3:
        if st.button("📋 View Inventory"):
            st.session_state.current_page = "View Inventory"
    with col4:
        if st.button("🗑️ Delete Items"):
            st.session_state.current_page = "Delete Items"

    if st.session_state.show_success:
        st.success(st.session_state.success_message, icon="✅")

    render_footer()

def add_item_page():
    render_header()
    st.title("➕ Add New Item")
    item_type = st.selectbox("Select Item Type", ["Perishable", "Electronic", "General"])
    name = st.text_input("Item Name")
    quantity = st.number_input("Quantity", min_value=1)
    price = st.number_input("Price", min_value=0.0, format="%.2f")

    if item_type == "Perishable":
        expiry = st.date_input("Expiry Date")
        item = PerishableItem(name=name, quantity=quantity, price=price, expiry_date=expiry)
    elif item_type == "Electronic":
        warranty = st.number_input("Warranty (years)", min_value=0)
        item = ElectronicItem(name=name, quantity=quantity, price=price, warranty_years=warranty)
    else:
        item = Item(name=name, quantity=quantity, price=price)

    if st.button("Add Item"):
        session = Session()
        session.add(item)
        session.commit()
        session.close()
        success_animation(f"Item '{name}' added successfully.")
        st.session_state.current_page = "Home"

    st.button("← Back to Home", on_click=lambda: setattr(st.session_state, 'current_page', 'Home'))
    render_footer()

def update_item_page():
    render_header()
    st.title("✏️ Update Existing Item")
    st.button("← Back to Home", on_click=lambda: setattr(st.session_state, 'current_page', 'Home'))

    session = Session()
    items = session.query(Item).all()
    if not items:
        st.warning("No items to update.")
        session.close()
        render_footer()
        return

    options = {f"{i.name} (ID: {i.item_id})": i.item_id for i in items}
    selection = st.selectbox("Select Item", list(options.keys()))
    item = session.query(Item).filter(Item.item_id == options[selection]).first()

    name = st.text_input("Item Name", item.name)
    quantity = st.number_input("Quantity", min_value=1, value=item.quantity)
    price = st.number_input("Price", min_value=0.0, format="%.2f", value=item.price)
    if isinstance(item, PerishableItem):
        expiry = st.date_input("Expiry Date", item.expiry_date)
    elif isinstance(item, ElectronicItem):
        warranty = st.number_input("Warranty", min_value=0, value=item.warranty_years)

    if st.button("💾 Save Changes"):
        item.name = name
        item.quantity = quantity
        item.price = price
        if isinstance(item, PerishableItem):
            item.expiry_date = expiry
        elif isinstance(item, ElectronicItem):
            item.warranty_years = warranty
        session.commit()
        session.close()
        success_animation(f"Item '{name}' updated successfully.")
        st.session_state.current_page = "Home"

    render_footer()

def view_inventory_page():
    render_header()
    st.title("📋 Inventory Overview")
    st.button("← Back to Home", on_click=lambda: setattr(st.session_state, 'current_page', 'Home'))

    session = Session()
    items = session.query(Item).all()
    if not items:
        st.warning("No inventory found.")
        session.close()
        render_footer()
        return

    view_mode = st.radio("View Mode", ["Cards", "Table"], horizontal=True)
    total_value = sum(item.calculate_total_price() for item in items)
    st.subheader(f"💰 Total Inventory Value: ${total_value:,.2f}")

    if view_mode == "Cards":
        for item in items:
            st.markdown("----")
            st.subheader(f"{item.name} (ID: {item.item_id})")
            st.write(f"📦 Quantity: {item.quantity}")
            st.write(f"💵 Price: ${item.price:.2f}")
            if isinstance(item, PerishableItem):
                st.write(f"📅 Expiry Date: {item.expiry_date}")
            elif isinstance(item, ElectronicItem):
                st.write(f"🛠 Warranty: {item.warranty_years} years")
            st.metric("Total Value", f"${item.calculate_total_price():,.2f}")
    else:
        data = []
        for i in items:
            row = {
                "ID": i.item_id,
                "Name": i.name,
                "Quantity": i.quantity,
                "Price": f"${i.price:.2f}",
                "Total": f"${i.calculate_total_price():,.2f}"
            }
            if isinstance(i, PerishableItem):
                row["Expiry Date"] = i.expiry_date
            elif isinstance(i, ElectronicItem):
                row["Warranty"] = f"{i.warranty_years} years"
            data.append(row)
        st.dataframe(pd.DataFrame(data), use_container_width=True)

    session.close()
    render_footer()

def delete_items_page():
    render_header()
    st.title("🗑️ Delete Items")
    st.button("← Back to Home", on_click=lambda: setattr(st.session_state, 'current_page', 'Home'))

    session = Session()
    items = session.query(Item).all()
    if not items:
        st.warning("No items to delete.")
        session.close()
        render_footer()
        return

    ids_to_delete = []
    for i in items:
        if st.checkbox(f"❌ {i.name} (ID: {i.item_id})"):
            ids_to_delete.append(i.item_id)

    if ids_to_delete and st.button("🚨 Delete Selected Items"):
        for id_ in ids_to_delete:
            obj = session.query(Item).filter(Item.item_id == id_).first()
            if obj:
                session.delete(obj)
        session.commit()
        session.close()
        success_animation(f"Deleted {len(ids_to_delete)} item(s).")
        st.rerun()

    render_footer()

# Router
page = st.session_state.current_page
if page == "Home":
    home_page()
elif page == "Add Item":
    add_item_page()
elif page == "Update Item":
    update_item_page()
elif page == "View Inventory":
    view_inventory_page()
elif page == "Delete Items":
    delete_items_page()
