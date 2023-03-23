ul_element = document.querySelector("#frameworks")
with open("names.txt") as f:
    for line in f:
        li_element = document.createElement("li")
        li_element.innerText = line
        ul_element.appendChild(li_element)