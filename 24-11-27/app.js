const showAddTodoBtn = document.getElementById("showAddTodo");
const todoList = document.getElementById("todoList");

let todos = JSON.parse(localStorage.getItem("todos")) || [];

// 할 일 리스트 렌더링
function renderTodos() {
  todoList.innerHTML = "";
  todos.forEach((todo, index) => {
    const todoItem = document.createElement("li");
    todoItem.className = "todo-item";

    // 체크박스
    const checkbox = document.createElement("input");
    checkbox.type = "checkbox";
    checkbox.checked = todo.completed;
    checkbox.addEventListener("change", () => toggleTodoCompletion(index, label));

    // 텍스트 또는 입력창
    const label = document.createElement("label");
    label.textContent = todo.text;
    label.className = todo.completed ? "completed" : "";
    label.style.display = todo.editing ? "none" : "inline";

    const input = document.createElement("input");
    input.type = "text";
    input.value = todo.text;
    input.style.display = todo.editing ? "inline" : "none";
    input.addEventListener("blur", () => saveEditedTodo(index, input.value));
    input.addEventListener("keypress", (e) => {
      if (e.key === "Enter") saveEditedTodo(index, input.value);
    });

    // 수정 버튼
    const editBtn = document.createElement("button");
    editBtn.textContent = "Edit";
    editBtn.addEventListener("click", () => toggleEditState(index));

    // 삭제 버튼
    const deleteBtn = document.createElement("button");
    deleteBtn.textContent = "Delete";
    deleteBtn.addEventListener("click", () => deleteTodo(index));

    // 요소 추가
    todoItem.appendChild(checkbox);
    todoItem.appendChild(label);
    todoItem.appendChild(input);
    todoItem.appendChild(editBtn);
    todoItem.appendChild(deleteBtn);
    todoList.appendChild(todoItem);
  });
}

// 체크박스 상태 변경
function toggleTodoCompletion(index, label) {
  todos[index].completed = !todos[index].completed;
  saveTodos();
  renderTodos(); // 리스트를 다시 렌더링
}

// 할 일 추가
function addTodo() {
  const newTodo = {
    text: "",
    completed: false,
    editing: true,
  };

  todos.push(newTodo);
  saveTodos();
  renderTodos();
}

// 수정 가능 상태 토글
function toggleEditState(index) {
  todos[index].editing = !todos[index].editing;
  saveTodos();
  renderTodos();
}

// 텍스트 저장
function saveEditedTodo(index, newValue) {
  if (newValue.trim() === "") {
    alert("Text cannot be empty.");
    return;
  }
  todos[index].text = newValue.trim();
  todos[index].editing = false;
  saveTodos();
  renderTodos();
}

// 할 일 삭제
function deleteTodo(index) {
  todos.splice(index, 1);
  saveTodos();
  renderTodos();
}

// LocalStorage에 저장
function saveTodos() {
  localStorage.setItem("todos", JSON.stringify(todos));
}

// 초기화
showAddTodoBtn.addEventListener("click", addTodo);

// 첫 렌더링
renderTodos();
