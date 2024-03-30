import streamlit as st

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi >= 18.5 and bmi < 25:
        return "Normal weight"
    elif bmi >= 25 and bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    st.title("BMI Calculator")
    st.write("Enter your weight and height to calculate BMI.")
    
    weight_unit = st.selectbox("Select weight unit", ["kg", "lbs"])
    height_unit = st.selectbox("Select height unit", ["m", "cm", "in"])

    weight = st.number_input(f"Enter your weight (in {weight_unit})", value=70.0)
    height = st.number_input(f"Enter your height (in {height_unit})", value=5.4)

    if weight_unit == "lbs":
        weight *= 0.453592  # Convert lbs to kg

    if height_unit == "cm":
        height /= 100  # Convert cm to meters
    elif height_unit == "in":
        height *= 0.0254  # Convert inches to meters

    if st.button("Calculate BMI"):
        bmi = calculate_bmi(weight, height)
        interpretation = interpret_bmi(bmi)
        st.write(f"Your BMI: {bmi:.2f}")
        st.write(f"Interpretation: {interpretation}")

if __name__ == "__main__":
    main()
