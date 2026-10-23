
import streamlit as st
from travel_data import destinations
from travel_assistant import answer_travel_question
from route_optimizer import optimize_route
from trip_manager import (
    save_trip,
    get_trips,
    delete_trip,
    add_expense,
    get_expenses,
    add_packing_item,
    update_packing_item,
    get_packing_list
)
from weather_service import get_weather, get_weather_description

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="WanderWise | Travel Planner",
    page_icon="🌍",
    layout="wide"
)


# --------------------------------------------------
# DESTINATION PHOTOS
# --------------------------------------------------

photos = {
    "Goa": "https://images.unsplash.com/photo-1512343879784-a960bf40e7f2",
    "Jaipur": "https://images.unsplash.com/photo-1599661046827-dacff0c0f09a",
    "Manali": "https://images.unsplash.com/photo-1626621341517-bbf3d9990a23",
    "Hyderabad": "https://images.unsplash.com/photo-1572445271230-a78b5944a659",
    "Ooty": "https://images.unsplash.com/photo-1597074866923-dc0589150358",
    "Kerala": "https://images.unsplash.com/photo-1602216056096-3b40cc0c9944",
    "Agra": "https://images.unsplash.com/photo-1564507592333-c60657eea523",
    "Darjeeling": "https://images.unsplash.com/photo-1544735716-392fe2489ffa",
    "Mumbai": "https://images.unsplash.com/photo-1570168007204-dfb528c6958f",
    "Delhi": "https://images.unsplash.com/photo-1587474260584-136574528ed5",
    "Kashmir": "https://images.unsplash.com/photo-1595815771614-ade9d652a65d",
    "Rishikesh": "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee",
    "Pondicherry": "https://images.unsplash.com/photo-1582510003544-4d00b7f74220",
    "Varanasi": "https://images.unsplash.com/photo-1561361513-2d000a50f0dc",
    "Andaman": "https://images.unsplash.com/photo-1510414842594-a61c69b5ae57"
}


def show_image(place):
    """Display the destination image when available."""

    image_url = photos.get(place)

    if image_url:
        st.image(image_url, use_container_width=True)
    else:
        st.info("A photo is not available for this destination yet.")


# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@500;600;700;800&display=swap');

    :root {
        --ww-ink: #142d3b;
        --ww-muted: #647783;
        --ww-teal: #087f8c;
        --ww-border: #dce8eb;
        --ww-card: #ffffff;
    }

    .stApp {
        background:
            radial-gradient(circle at 8% 2%, rgba(198, 235, 231, 0.40), transparent 26rem),
            linear-gradient(180deg, #f7fafb 0%, #f2f7f8 100%);
        color: var(--ww-ink);
        font-family: 'DM Sans', sans-serif;
    }

    .block-container {
        max-width: 1240px;
        padding-top: 1.8rem;
        padding-bottom: 2.5rem;
    }

    h1, h2, h3, h4 {
        color: var(--ww-ink);
        font-family: 'Manrope', sans-serif;
        letter-spacing: -0.025em;
    }

    p, label, [data-testid="stMarkdownContainer"] {
        color: var(--ww-ink);
    }

    .ww-hero {
        position: relative;
        overflow: hidden;
        padding: 2.4rem 2.6rem;
        border-radius: 26px;
        background: linear-gradient(118deg, #102f43 0%, #086f78 58%, #35a6a0 100%);
        color: #ffffff;
        box-shadow: 0 18px 42px rgba(18, 61, 75, 0.17);
        margin-bottom: 1.25rem;
    }

    .ww-hero:after {
        content: "";
        position: absolute;
        width: 250px;
        height: 250px;
        right: -55px;
        top: -105px;
        border-radius: 50%;
        border: 1px solid rgba(255,255,255,0.22);
        box-shadow: 0 0 0 28px rgba(255,255,255,0.05),
                    0 0 0 58px rgba(255,255,255,0.04);
    }

    .ww-eyebrow {
        display: inline-block;
        padding: 6px 11px;
        margin-bottom: 13px;
        border: 1px solid rgba(255,255,255,0.28);
        border-radius: 999px;
        background: rgba(255,255,255,0.10);
        color: #e5ffff;
        font-size: 0.78rem;
        font-weight: 700;
        letter-spacing: 0.09em;
        text-transform: uppercase;
    }

    .ww-hero-title {
        position: relative;
        z-index: 1;
        color: #ffffff !important;
        font-family: 'Manrope', sans-serif;
        font-size: clamp(2.2rem, 5vw, 3.7rem);
        line-height: 1.08;
        font-weight: 800;
        letter-spacing: -0.05em;
        margin: 0 0 0.7rem 0;
    }

    .ww-hero-copy {
        position: relative;
        z-index: 1;
        color: #e1f4f3 !important;
        max-width: 650px;
        font-size: 1.05rem;
        line-height: 1.65;
        margin-bottom: 1.2rem;
    }

    .ww-pill-row {
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
        position: relative;
        z-index: 1;
    }

    .ww-pill {
        display: inline-block;
        padding: 7px 12px;
        border-radius: 999px;
        background: rgba(255,255,255,0.13);
        border: 1px solid rgba(255,255,255,0.18);
        color: #ffffff !important;
        font-size: 0.82rem;
        font-weight: 600;
    }

    .section-title {
        color: var(--ww-ink);
        font-family: 'Manrope', sans-serif;
        font-size: 1.55rem;
        font-weight: 800;
        letter-spacing: -0.035em;
        padding-bottom: 0.45rem;
        border-bottom: 2px solid #dcebed;
        margin-top: 0.25rem;
        margin-bottom: 0.6rem;
    }

    [data-testid="stMetric"] {
        background: var(--ww-card);
        padding: 17px 18px;
        border-radius: 16px;
        border: 1px solid var(--ww-border);
        box-shadow: 0 5px 16px rgba(20, 58, 71, 0.045);
    }

    [data-testid="stMetricLabel"] {
        color: var(--ww-muted);
        font-weight: 600;
    }

    [data-testid="stMetricValue"] {
        color: var(--ww-ink);
        font-family: 'Manrope', sans-serif;
        font-weight: 800;
    }

    [data-testid="stVerticalBlockBorderWrapper"] {
        border-radius: 18px;
    }

    [data-testid="stExpander"] {
        background: rgba(255,255,255,0.84);
        border: 1px solid var(--ww-border);
        border-radius: 14px;
        overflow: hidden;
    }

    [data-testid="stTextInput"] input,
    [data-testid="stNumberInput"] input,
    [data-testid="stSelectbox"] div[data-baseweb="select"],
    [data-testid="stMultiSelect"] div[data-baseweb="select"] {
        border-radius: 10px;
    }

    div.stButton > button,
    div[data-testid="stFormSubmitButton"] > button {
        background: linear-gradient(110deg, #087f8c, #119a99);
        color: #ffffff;
        border: 0;
        border-radius: 11px;
        min-height: 2.7rem;
        padding: 0.65rem 1rem;
        font-weight: 700;
        transition: all 0.18s ease-in-out;
        box-shadow: 0 5px 12px rgba(8, 127, 140, 0.13);
    }

    div.stButton > button:hover,
    div[data-testid="stFormSubmitButton"] > button:hover {
        background: linear-gradient(110deg, #06636d, #087f8c);
        color: #ffffff;
        border: 0;
        transform: translateY(-1px);
        box-shadow: 0 8px 18px rgba(8, 127, 140, 0.2);
    }

    div.stButton > button:focus,
    div[data-testid="stFormSubmitButton"] > button:focus {
        color: #ffffff;
        border: 2px solid #7bd4d1;
    }

    [data-testid="stAlert"] {
        border-radius: 12px;
    }

    [data-testid="stDataFrame"] {
        border: 1px solid var(--ww-border);
        border-radius: 12px;
        overflow: hidden;
    }

    hr {
        border-color: #dce8eb;
        margin-top: 1.5rem;
        margin-bottom: 1.5rem;
    }

    .ww-footer {
        text-align: center;
        color: var(--ww-muted);
        padding: 1.4rem 0 0.5rem 0;
        font-size: 0.9rem;
    }

    @media (max-width: 700px) {
        .block-container {
            padding-left: 1rem;
            padding-right: 1rem;
            padding-top: 1rem;
        }
        .ww-hero {
            padding: 1.7rem 1.35rem;
            border-radius: 20px;
        }
        .ww-hero-copy {
            font-size: 0.95rem;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)


# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.markdown(
    """
    <section class="ww-hero">
        <div class="ww-eyebrow">Your personal travel companion</div>
        <div class="ww-hero-title">WanderWise <span aria-hidden="true">✦</span></div>
        <div class="ww-hero-copy">
            Plan meaningful journeys with smart cost estimates, AI travel
            guidance, saved itineraries, packing lists, and weather updates —
            all in one place.
        </div>
        <div class="ww-pill-row">
            <span class="ww-pill">✈️ Trip planning</span>
            <span class="ww-pill">🤖 Gemini AI</span>
            <span class="ww-pill">🗺️ Route costs</span>
            <span class="ww-pill">🌦️ Weather</span>
        </div>
    </section>
    """,
    unsafe_allow_html=True
)

st.caption("DISCOVER  ·  PLAN  ·  TRAVEL WITH CONFIDENCE")

st.divider()


# --------------------------------------------------
# TRIP PLANNER
# --------------------------------------------------

st.markdown(
    '<div class="section-title">✈️ Plan Your Trip</div>',
    unsafe_allow_html=True
)

st.write(
    "Choose one destination, set your preferences, "
    "and discover a trip that suits your budget."
)

left, right = st.columns([1, 1.2], gap="large")


with left:
    st.subheader("Your Travel Preferences")

    # Destination dropdown
    destination_options = sorted(destinations.keys())

    destination = st.selectbox(
        "📍 Select your destination",
        options=["Select a destination"] + destination_options,
        index=0,
        key="selected_destination"
    )

    if destination == "Select a destination":
        destination = ""

    # Trip duration
    days = st.number_input(
        "🗓️ Number of days",
        min_value=1,
        max_value=30,
        value=3,
        step=1
    )

    # Interests available in the selected destination
    selected_interests = []

    if destination:
        destination_info = destinations.get(destination, {})
        available_interests = destination_info.get("type", [])

        if isinstance(available_interests, str):
            available_interests = [available_interests]

        if available_interests:
            selected_interests = st.multiselect(
                "🎯 What are you interested in?",
                options=available_interests,
                default=available_interests[:1]
            )
        else:
            st.info(
                "No specific interests are listed for this destination."
            )

    # Budget
    budget = st.number_input(
        "💰 Your total budget (₹)",
        min_value=1000,
        max_value=1000000,
        value=10000,
        step=1000
    )

    plan_button = st.button(
        "✨ Plan My Trip",
        use_container_width=True
    )


with right:
    st.subheader("Your Destination")

    if destination:
        show_image(destination)

        st.markdown(f"### 📍 {destination}")

        destination_info = destinations.get(destination, {})

        description = destination_info.get(
            "description",
            f"Discover the attractions and experiences of {destination}."
        )

        st.write(description)

        if selected_interests:
            st.write(
                "**Your interests:** "
                + ", ".join(selected_interests)
            )
    else:
        st.info(
            "Select a destination from the dropdown to see its details."
        )

        st.markdown(
            """
            ### 🌄 Where would you like to go?

            Explore destinations, choose your interests, and plan
            a trip according to your budget.
            """
        )


# --------------------------------------------------
# TRIP PLAN RESULTS
# --------------------------------------------------

if plan_button:

    if not destination:
        st.warning("Please select a destination first.")

    else:
        destination_info = destinations.get(destination, {})

        # Read cost information safely
        travel_cost = destination_info.get("travel_cost", 0)
        hotel_per_day = destination_info.get("hotel_per_day", 0)
        activities = destination_info.get("activities", {})

        # Convert cost values to numbers
        try:
            travel_cost = float(travel_cost)
        except (ValueError, TypeError):
            travel_cost = 0

        try:
            hotel_per_day = float(hotel_per_day)
        except (ValueError, TypeError):
            hotel_per_day = 0

        # Support activity costs stored as a dictionary or list
        if isinstance(activities, dict):
            activity_cost = 0

            for value in activities.values():
                try:
                    activity_cost += float(value)
                except (ValueError, TypeError):
                    continue

            activity_names = list(activities.keys())

        elif isinstance(activities, list):
            activity_cost = 0
            activity_names = activities

        else:
            activity_cost = 0
            activity_names = []

        total_hotel_cost = hotel_per_day * days
        total_estimated_cost = (
            travel_cost + total_hotel_cost + activity_cost
        )

        st.divider()
        st.markdown(
            '<div class="section-title">🧳 Your Trip Plan</div>',
            unsafe_allow_html=True
        )

        metric1, metric2, metric3 = st.columns(3)

        with metric1:
            st.metric("📍 Destination", destination)

        with metric2:
            st.metric("🗓️ Duration", f"{days} days")

        with metric3:
            st.metric(
                "💰 Estimated Cost",
                f"₹{total_estimated_cost:,.0f}"
            )

        st.subheader("💵 Estimated Budget Breakdown")

        cost_col1, cost_col2, cost_col3 = st.columns(3)

        with cost_col1:
            st.metric("Travel", f"₹{travel_cost:,.0f}")

        with cost_col2:
            st.metric(
                "Accommodation",
                f"₹{total_hotel_cost:,.0f}"
            )

        with cost_col3:
            st.metric(
                "Activities",
                f"₹{activity_cost:,.0f}"
            )

        # Budget comparison
        if total_estimated_cost <= budget:
            st.success(
                f"Great! Your estimated cost is within your "
                f"₹{budget:,.0f} budget."
            )
        else:
            st.warning(
                f"Your estimated cost exceeds your budget by "
                f"₹{total_estimated_cost - budget:,.0f}. "
                "Consider reducing accommodation or activity costs."
            )

        # Selected interests
        st.subheader("🎯 Your Selected Interests")

        if selected_interests:
            for interest in selected_interests:
                st.write(f"✅ {interest}")
        else:
            st.write(
                "No interests selected. You can still explore "
                "the destination."
            )

        # Suggested activities
        st.subheader("🏛️ Suggested Activities")

        if activity_names:
            for activity in activity_names:
                st.write(f"• {activity}")
        else:
            st.write(
                "No activities have been added to the dataset for "
                "this destination yet."
            )

        st.caption(
            "Note: These are approximate estimates. Actual costs may "
            "vary depending on travel dates, accommodation, transport, "
            "and activities. Confirm prices before booking."
        )


# --------------------------------------------------
# AI TRAVEL CHATBOT
# --------------------------------------------------

st.divider()

st.markdown(
    '<div class="section-title">🤖 Ask WanderWise AI</div>',
    unsafe_allow_html=True
)

st.write(
    "Ask questions about destinations, sightseeing, packing, "
    "travel tips, or planning your holiday."
)

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display earlier messages
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
user_question = st.chat_input(
    "Ask me anything about travel..."
)

if user_question:
    st.session_state.chat_history.append(
        {
            "role": "user",
            "content": user_question
        }
    )

    with st.chat_message("user"):
        st.markdown(user_question)

    with st.chat_message("assistant"):
        with st.spinner("WanderWise is thinking..."):

            try:
                ai_answer = answer_travel_question(user_question)

                if not ai_answer:
                    ai_answer = (
                        "Sorry, I couldn't generate a response. "
                        "Please try asking in a different way."
                    )

                st.markdown(ai_answer)

            except Exception as error:
                ai_answer = (
                    "Sorry, I couldn't connect to the AI travel "
                    "assistant. Please check your Gemini API key, "
                    "internet connection, and model configuration."
                )

                st.error(ai_answer)

                # Print technical details in the terminal for debugging
                print("Travel assistant error:", error)

    st.session_state.chat_history.append(
        {
            "role": "assistant",
            "content": ai_answer
        }
    )


# --------------------------------------------------
# MULTI-DESTINATION ROUTE OPTIMIZER
# --------------------------------------------------

st.divider()

st.markdown(
    '<div class="section-title">'
    '🗺️ Multi-Destination Route Optimizer'
    '</div>',
    unsafe_allow_html=True
)

st.write(
    "Select multiple destinations to create a cost-based "
    "itinerary and estimate your total trip expenses."
)

route_destinations = st.multiselect(
    "📍 Choose your destinations",
    options=sorted(destinations.keys()),
    key="route_destinations"
)

days_per_destination = st.number_input(
    "🗓️ Days at each destination",
    min_value=1,
    max_value=30,
    value=2,
    step=1,
    key="route_days"
)

route_budget = st.number_input(
    "💰 Total route budget (₹)",
    min_value=1000,
    max_value=10000000,
    value=30000,
    step=1000,
    key="route_budget"
)

if st.button("🚀 Optimize My Route", key="optimize_route_button"):

    if not route_destinations:
        st.warning("Please select at least one destination.")

    else:
        result = optimize_route(
            route_destinations,
            days_per_destination
        )

        if not result["details"]:
            st.error(result["message"])

        else:
            st.success(result["message"])

            st.subheader("🧭 Your Cost-Based Itinerary")

            for index, place in enumerate(result["details"], start=1):
                with st.expander(
                    f"{index}. {place['destination']} — "
                    f"₹{place['total_cost']:,.0f}"
                ):
                    col1, col2 = st.columns(2)

                    with col1:
                        st.write(
                            f"🚆 Travel: ₹{place['travel_cost']:,.0f}"
                        )
                        st.write(
                            f"🏨 Accommodation: ₹{place['hotel_cost']:,.0f}"
                        )

                    with col2:
                        st.write(
                            f"🎟️ Activities: ₹{place['activity_cost']:,.0f}"
                        )
                        st.write(
                            f"🗓️ Duration: {place['days']} days"
                        )

            metric1, metric2 = st.columns(2)

            with metric1:
                st.metric(
                    "Estimated Total Cost",
                    f"₹{result['total_cost']:,.0f}"
                )

            with metric2:
                st.metric(
                    "Total Duration",
                    f"{len(result['route']) * days_per_destination} days"
                )

            if result["total_cost"] <= route_budget:
                st.success(
                    f"Your estimated cost is within your "
                    f"₹{route_budget:,.0f} budget."
                )
            else:
                st.warning(
                    f"You are over budget by "
                    f"₹{result['total_cost'] - route_budget:,.0f}."
                )

            st.write("**Suggested destination order:**")

            st.markdown(
                " → ".join(result["route"])
            )

            st.caption(
                "The order is based on estimated cost, from lowest "
                "to highest. It does not represent the shortest "
                "geographical route. Costs are estimates, not live prices."
            )


# --------------------------------------------------
# TRIP MANAGER
# --------------------------------------------------

st.divider()

st.markdown(
    '<div class="section-title">🧳 My Trip Manager</div>',
    unsafe_allow_html=True
)

st.write(
    "Save itineraries, record travel expenses, and manage packing lists."
)

# Save a new trip
with st.expander("➕ Save a New Trip", expanded=False):

    save_destination = st.selectbox(
        "Choose destination",
        options=sorted(destinations.keys()),
        key="save_trip_destination"
    )

    save_days = st.number_input(
        "Number of days",
        min_value=1,
        max_value=30,
        value=3,
        key="save_trip_days"
    )

    save_budget = st.number_input(
        "Trip budget (₹)",
        min_value=1000,
        max_value=1000000,
        value=10000,
        step=1000,
        key="save_trip_budget"
    )

    if st.button("💾 Save Trip", key="save_trip_button"):
        trip_id = save_trip(
            save_destination,
            save_days,
            save_budget
        )

        st.session_state["selected_managed_trip"] = trip_id
        st.success("Trip saved successfully!")

# Load saved trips
saved_trips = get_trips()

if saved_trips:

    trip_options = {
        f"{trip['destination']} — {trip['days']} days "
        f"(Budget ₹{trip['budget']:,.0f}) | {trip['id']}": trip["id"]
        for trip in saved_trips
    }

    selected_trip_label = st.selectbox(
        "📂 Select a saved trip",
        options=list(trip_options.keys()),
        key="managed_trip_selector"
    )

    selected_trip_id = trip_options[selected_trip_label]

    selected_trip = next(
        trip for trip in saved_trips
        if trip["id"] == selected_trip_id
    )

    st.subheader(f"📍 {selected_trip['destination']}")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Duration", f"{selected_trip['days']} days")

    with col2:
        st.metric("Budget", f"₹{selected_trip['budget']:,.0f}")

    # Expenses
    st.markdown("### 💸 Track Expenses")

    with st.form("add_expense_form", clear_on_submit=True):

        expense_description = st.text_input(
            "Expense description",
            placeholder="Example: Hotel, food, transport"
        )

        expense_amount = st.number_input(
            "Amount (₹)",
            min_value=0.0,
            max_value=1000000.0,
            value=100.0,
            step=50.0
        )

        expense_submitted = st.form_submit_button("➕ Add Expense")

    if expense_submitted:

        if not expense_description.strip():
            st.warning("Please enter an expense description.")

        elif expense_amount <= 0:
            st.warning("Expense amount must be greater than zero.")

        else:
            success = add_expense(
                selected_trip_id,
                expense_description.strip(),
                expense_amount
            )

            if success:
                st.success("Expense added successfully!")
                st.rerun()

    expenses = get_expenses(selected_trip_id)

    total_expenses = sum(
        expense["amount"] for expense in expenses
    )

    st.metric("Total Recorded Expenses", f"₹{total_expenses:,.2f}")

    if expenses:
        st.dataframe(
            [
                {
                    "Date": expense["date"],
                    "Description": expense["description"],
                    "Amount (₹)": expense["amount"]
                }
                for expense in expenses
            ],
            use_container_width=True,
            hide_index=True
        )
    else:
        st.info("No expenses recorded for this trip yet.")

    remaining_budget = selected_trip["budget"] - total_expenses

    if remaining_budget >= 0:
        st.success(f"Remaining budget: ₹{remaining_budget:,.2f}")
    else:
        st.warning(f"Over budget by ₹{-remaining_budget:,.2f}")

    # Packing list
    st.markdown("### 🎒 Packing List")

    with st.form("add_packing_item_form", clear_on_submit=True):

        packing_item = st.text_input(
            "Item to pack",
            placeholder="Example: Clothes, charger, medicines"
        )

        packing_submitted = st.form_submit_button("➕ Add Item")

    if packing_submitted:

        if not packing_item.strip():
            st.warning("Please enter an item.")

        else:
            add_packing_item(
                selected_trip_id,
                packing_item.strip()
            )
            st.success("Packing item added!")
            st.rerun()

    packing_items = get_packing_list(selected_trip_id)

    if packing_items:

        for index, item in enumerate(packing_items):

            checked = st.checkbox(
                item["item"],
                value=item["packed"],
                key=f"packing_{selected_trip_id}_{index}"
            )

            if checked != item["packed"]:
                update_packing_item(
                    selected_trip_id,
                    item["item"],
                    checked
                )
                st.rerun()

        packed_count = sum(
            1 for item in packing_items if item["packed"]
        )

        st.caption(
            f"{packed_count} of {len(packing_items)} items packed."
        )

    else:
        st.info("Your packing list is empty.")

    # Delete trip
    with st.expander("🗑️ Delete This Trip"):

        confirm_delete = st.checkbox(
            "I want to permanently delete this trip and its records.",
            key=f"confirm_delete_{selected_trip_id}"
        )

        if st.button(
            "Delete Trip",
            key=f"delete_trip_{selected_trip_id}"
        ):

            if confirm_delete:
                delete_trip(selected_trip_id)

                st.session_state.pop(
                    "managed_trip_selector", None
                )

                st.success("Trip and its records deleted.")
                st.rerun()

            else:
                st.warning("Please confirm before deleting.")

else:
    st.info(
        "You haven't saved any trips yet. Use 'Save a New Trip' above."
    )


# --------------------------------------------------
# WEATHER SERVICE
# --------------------------------------------------

st.divider()

st.markdown(
    '<div class="section-title">🌦️ Travel Weather</div>',
    unsafe_allow_html=True
)

st.write(
    "Check current weather and the 7-day forecast "
    "before planning your journey."
)

weather_city = st.selectbox(
    "📍 Select a city",
    options=sorted(destinations.keys()),
    key="weather_city"
)

if st.button("🌤️ Check Weather", key="check_weather_button"):

    with st.spinner("Fetching the latest weather information..."):
        weather_result = get_weather(weather_city)

    if not weather_result["success"]:
        st.error(weather_result["message"])

    else:
        current = weather_result["current"]
        daily = weather_result["daily"]

        st.subheader(
            f"Weather in {weather_result['city']}, "
            f"{weather_result['country']}"
        )

        description = get_weather_description(
            current.get("weather_code")
        )

        st.info(f"Current conditions: {description}")

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(
                "🌡️ Temperature",
                f"{current.get('temperature_2m', 'N/A')} °C"
            )

        with col2:
            st.metric(
                "🤗 Feels Like",
                f"{current.get('apparent_temperature', 'N/A')} °C"
            )

        with col3:
            st.metric(
                "💧 Humidity",
                f"{current.get('relative_humidity_2m', 'N/A')}%"
            )

        with col4:
            st.metric(
                "💨 Wind Speed",
                f"{current.get('wind_speed_10m', 'N/A')} km/h"
            )

        st.subheader("📅 7-Day Forecast")

        forecast_rows = []

        dates = daily.get("time", [])

        for i, date in enumerate(dates):
            code = daily.get("weather_code", [])
            max_temps = daily.get("temperature_2m_max", [])
            min_temps = daily.get("temperature_2m_min", [])
            rain = daily.get("precipitation_probability_max", [])

            forecast_rows.append({
                "Date": date,
                "Conditions": get_weather_description(
                    code[i] if i < len(code) else None
                ),
                "Max Temp (°C)": (
                    max_temps[i] if i < len(max_temps) else "N/A"
                ),
                "Min Temp (°C)": (
                    min_temps[i] if i < len(min_temps) else "N/A"
                ),
                "Rain Chance (%)": (
                    rain[i] if i < len(rain) else "N/A"
                )
            })

        if forecast_rows:
            st.dataframe(
                forecast_rows,
                use_container_width=True,
                hide_index=True
            )
        else:
            st.info("No forecast data is currently available.")

        st.caption(
            "Weather information is provided by Open-Meteo. "
            "Forecasts can change; check again closer to your trip."
        )


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.divider()

st.markdown(
    """
    <div class="ww-footer">
        <strong>🌍 WanderWise</strong> · Intelligent Travel Bot
        <br>
        Plan smarter. Travel better. ✨
    </div>
    """,
    unsafe_allow_html=True
)
