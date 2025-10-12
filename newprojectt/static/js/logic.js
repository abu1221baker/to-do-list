let task_complete = document.querySelectorAll(".checkbox");

// Load saved state from localStorage
task_complete.forEach((line) => {
    let parent = line.closest("div"); // Or li if that's your structure
    let title = parent.querySelector(".todo-title");
    let taskKey = `checkbox-${title.textContent.trim()}`;

    const isChecked = localStorage.getItem(taskKey) === "true";
    line.checked = isChecked;

    if (isChecked) {
        title.style.textDecoration = "line-through";
        title.style.color = "lightgreen";
    } else {
        title.style.textDecoration = "none";
        title.style.color = "";
    }

    // Add event listener for changes
    line.addEventListener("click", () => {
        localStorage.setItem(taskKey, line.checked);

        if (line.checked) {
            title.style.textDecoration = "line-through";
            title.style.color = "lightgreen";
        } else {
            title.style.textDecoration = "none";
            title.style.color = "";
        }
    });
});
document.querySelectorAll(".delete-btn").forEach((btn) => {
    btn.addEventListener("click", () => {
        const parent = btn.closest("div");
        const title = parent.querySelector(".todo-title");
        const taskKey = `checkbox-${title.textContent.trim()}`;
        
        localStorage.removeItem(taskKey);
        parent.remove(); // Or your method to remove the task element
    });
});
