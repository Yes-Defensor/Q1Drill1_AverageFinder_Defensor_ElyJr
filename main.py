from js import document
from pyodide.ffi import create_proxy

# This function calculates the average of two quiz scores
def compute_average(event):
    score1 = float(document.getElementById("score1").value or 0)
    score2 = float(document.getElementById("score2").value or 0)
    average = (score1 + score2) / 2

    # Display the result with pass/fail message
    result_div = document.getElementById("result")
    if average >= 75:
        result_div.innerHTML = f"Average: {average:.2f} ✅ Passed"
    else:
        result_div.innerHTML = f"Average: {average:.2f} ❌ Failed"

# Bind the button click to the Python function
button = document.getElementById("compute-btn")
button.addEventListener("click", create_proxy(compute_average))
