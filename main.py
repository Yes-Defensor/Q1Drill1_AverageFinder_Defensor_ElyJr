from js import document  # Import the JavaScript document object to access HTML elements
from pyodide.ffi import create_proxy  # Import create_proxy to handle JavaScript events in Python

#  Function to compute the average of two quiz scores
def compute_average(event):
    # Get the value from the input field with ID "score1" and convert it to float
    # If the field is empty, default to 0
    score1 = float(document.getElementById("score1").value or 0)

    # Get the value from the input field with ID "score2" and convert it to float
    # If the field is empty, default to 0
    score2 = float(document.getElementById("score2").value or 0)

    # Calculate the average of the two scores
    average = (score1 + score2) / 2

    # 🎯 Display the result in the HTML element with ID "result"
    result_div = document.getElementById("result")

    # Show a pass/fail message based on the average score
    if average >= 75:
        result_div.innerHTML = f"Average: {average:.2f} ✅ Passed"
    else:
        result_div.innerHTML = f"Average: {average:.2f} ❌ Failed"

#  Bind the button click event to the compute_average function
# This ensures the function runs when the button with ID "compute-btn" is clicked
button = document.getElementById("compute-btn")
button.addEventListener("click", create_proxy(compute_average))
