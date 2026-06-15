 import streamlit as st

st.set_page_config(
    page_title="MiniStore",
    page_icon="🛍️",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background-color: #f5f7fb;
}

.hero {
    background: linear-gradient(135deg, #4F46E5, #7C3AED);
    padding: 40px;
    border-radius: 20px;
    color: white;
    text-align: center;
    margin-bottom: 30px;
}

.product-card {
    background: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
    margin-bottom: 20px;
    height: 260px;
}

.product-title {
    font-size: 1.2rem;
    font-weight: bold;
    color: #111827;
}

.product-price {
    color: #16a34a;
    font-size: 1.1rem;
    font-weight: bold;
}

.product-category {
    display: inline-block;
    background: #EEF2FF;
    color: #4F46E5;
    padding: 4px 10px;
    border-radius: 20px;
    font-size: 0.8rem;
}

.section-title {
    font-size: 2rem;
    font-weight: 700;
    color: #111827;
}

/* Floating support button */
.floating-button {
    position: fixed;
    bottom: 25px;
    right: 25px;
    background: #4F46E5;
    color: white !important;
    padding: 15px 22px;
    border-radius: 50px;
    text-decoration: none;
    font-weight: bold;
    box-shadow: 0px 6px 18px rgba(0,0,0,0.25);
    z-index: 9999;
}

.floating-button:hover {
    background: #3730A3;
}
</style>
""", unsafe_allow_html=True)

# Product data
products = [
    {"name": "Wireless Bluetooth Headphones", "price": 79.99, "description": "Premium over-ear headphones with noise cancellation and 30-hour battery life.", "category": "Electronics"},
    {"name": "Smart Fitness Watch", "price": 129.99, "description": "Track your health, workouts, sleep, and notifications in real-time.", "category": "Wearables"},
    {"name": "Mechanical Keyboard", "price": 89.99, "description": "RGB backlit keyboard with tactile switches for productivity and gaming.", "category": "Electronics"},
    {"name": "Minimalist Backpack", "price": 54.99, "description": "Stylish and durable backpack designed for work, travel, and everyday use.", "category": "Fashion"},
    {"name": "Portable Coffee Maker", "price": 39.99, "description": "Brew fresh coffee anywhere with this compact travel-friendly coffee maker.", "category": "Home & Kitchen"},
    {"name": "LED Desk Lamp", "price": 29.99, "description": "Modern desk lamp with adjustable brightness and eye-care lighting technology.", "category": "Home & Kitchen"}
]

# Sidebar
st.sidebar.title("🛍️ MiniStore")

categories = ["All"] + sorted(list(set(product["category"] for product in products)))
selected_category = st.sidebar.selectbox("Browse Categories", categories)

st.sidebar.markdown("---")
st.sidebar.subheader("🛒 Shopping Cart")
st.sidebar.write("Items: **3**")
st.sidebar.write("Subtotal: **$249.97**")
st.sidebar.write("Shipping: **Free**")
st.sidebar.success("Total: $249.97")

# Homepage hero
st.markdown("""
<div class="hero">
    <h1>🛍️ MiniStore</h1>
    <p>Your one-stop destination for premium gadgets, lifestyle products, and everyday essentials.</p>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="section-title">Welcome to MiniStore</div>', unsafe_allow_html=True)

st.write("""
Discover high-quality products carefully selected to enhance your lifestyle.
Browse our featured collection and find the perfect item for your needs.
""")

# Filter products
if selected_category == "All":
    filtered_products = products
else:
    filtered_products = [
        product for product in products
        if product["category"] == selected_category
    ]

st.markdown('<div class="section-title">Featured Products</div>', unsafe_allow_html=True)

# Product cards
cols = st.columns(3)

for index, product in enumerate(filtered_products):
    with cols[index % 3]:
        st.markdown(f"""
        <div class="product-card">
            <div class="product-category">{product['category']}</div>
            <div class="product-title">{product['name']}</div>
            <div class="product-price">${product['price']:.2f}</div>
            <p>{product['description']}</p>
        </div>
        """, unsafe_allow_html=True)

        st.button("Add to Cart", key=f"cart_{index}")

# Floating support button
st.markdown("""
<a class="floating-button" href="/Support_Chatbot" target="_self">
    💬 Support
</a>
""", unsafe_allow_html=True)

st.markdown("---")
st.markdown(
    "<center>© 2026 MiniStore • Demo E-Commerce Website Built with Streamlit</center>",
    unsafe_allow_html=True
)

