const list = document.getElementById('list');
const createBtn = document.getElementById('create-btn');
const sortByDateBtn = document.getElementById('sort-by-date');
const sortByPriorityBtn = document.getElementById('sort-by-priority');

let todos = [];

//추가버튼 누르면 생성
createBtn.addEventListener('click', createNewTodo);

//버튼 누를때 실행할 함수
function createNewTodo() {
    const item = {
        id: new Date().getTime(),
        text: '',
        complete: false,
        priority: Math.floor(Math.random() * 3) + 1
    }

    // 배열 처음에 새로운 아이템을 추가
    todos.unshift(item);

    // 요소 생성하기
    const {itemEl, inputEl, editBtnEl, removeBtnEl} = createTodoElement(item);

    // item을 list에 넣기
    list.prepend(itemEl);

    // diabled 지우기
    inputEl.removeAttribute('disabled');

    // 입력창에 포커싱
    inputEl.focus();
    saveToLocalStorage();
}

// 날짜순 정렬
sortByDateBtn.addEventListener('click', () => {
    todos.sort((a, b) => a.id - b.id); // 오름차순 (날짜가 오래된 순)
    renderTodoList(todos); // 화면 업데이트
});

// 중요도순 정렬
sortByPriorityBtn.addEventListener('click', () => {
    todos.sort((a, b) => b.priority - a.priority); // 내림차순 (높은 중요도 우선)
    renderTodoList(todos); // 화면 업데이트
});

// 렌더링 함수
function renderTodoList(todoList) {
    list.innerHTML = ''; // 기존 항목 초기화
    todoList.forEach(item => {
        const { itemEl } = createTodoElement(item);
        list.append(itemEl); // 정렬된 순서로 렌더링
    });
}

// 요소생성 함수(먼저 다 만들고, 자기 위치에 넣기)
function createTodoElement(item) {
    //div만들고 class를 item이라고 해라
    const itemEl = document.createElement('div');
    itemEl.classList.add('item');

    const checkboxEl = document.createElement('input');
    checkboxEl.type = 'checkbox';
    checkboxEl.checked = item.complete;

    if(item.complete) {
        itemEl.classList.add('complete');
    }
    saveToLocalStorage();

    const inputEl = document.createElement('input');
    inputEl.type = 'text';
    inputEl.value = item.text;
    inputEl.setAttribute('disabled','');
    
    const priorityEl = document.createElement('span'); // 중요도 표시
    priorityEl.textContent = `중요도: ${item.priority}`;
    priorityEl.style.marginLeft = '10px';

    // div 만들고 class를 actions라고 달아라라
    const actionsEl = document.createElement('div');
    actionsEl.classList.add('actions');

    // 버튼 만들기. class이름붙이기. 내부텍스트 채우기기
    const editBtnEl = document.createElement('button');
    editBtnEl.classList.add('material-icons');
    editBtnEl.innerText = 'edit';

    const removeBtnEl = document.createElement('button');
    removeBtnEl.classList.add('material-icons', 'remove-btn');
    removeBtnEl.innerText = 'remove_circle';

    // 입력이벤트 발생하면, 입력값을 넣어주기
    inputEl.addEventListener('input', ()=> {
        item.text = inputEl.value
    })

    // blur 발생하면, disabled 속성을 넣어주기
    inputEl.addEventListener('blur', ()=> {
        inputEl.setAttribute('disabled','');
        saveToLocalStorage();
    })

    // edit클릭하면, disabled를 지우기
    editBtnEl.addEventListener('click', ()=> {
        inputEl.removeAttribute('disabled');
        inputEl.focus();
    })
    
    // remove클릭하면, disabled를 지우기
    removeBtnEl.addEventListener('click', ()=> {
        // 이 작업은 배열에 있는 내용만 지움.
        todos = todos.filter(t => t.id !== item.id)
        
        // 요소지우기
        itemEl.remove();
        saveToLocalStorage();
    })
    
    // 변경 이벤트 발생하면, checked로 변경
    checkboxEl.addEventListener('change',() => {
        item.complete = checkboxEl.checked;

        // complete이면 class에 complete를 넣고, 아니면 지워라
        if(item.complete) {
            itemEl.classList.add('complete')
        } else {
            itemEl.classList.remove('complete');
        }
        saveToLocalStorage();
    })

    // 구조에 맞게 넣기
    itemEl.append(checkboxEl);
    itemEl.append(inputEl);
    itemEl.append(actionsEl);
    itemEl.append(priorityEl); // 중요도 추가

    actionsEl.append(editBtnEl);
    actionsEl.append(removeBtnEl);

    return {itemEl, inputEl, editBtnEl, removeBtnEl }
}

//로컬스토리지(string타입으로 넣어야함)
function saveToLocalStorage() {
    const data = JSON.stringify(todos); //todos는 배열상태라서

    window.localStorage.setItem('my_todos',data);
}

//저장된거 가져오기(string을 다시 배열로)
function loadFromLocalStorage() {
    const data = localStorage.getItem('my_todos');
    if(data) {
        todos = JSON.parse(data);
    }
}

//배열 순회하면서 만들어라
function displayTodos() {
    //데이터 가져오기기
    loadFromLocalStorage();

    for (let i = 0; i <todos.length; i++) {
        const item = todos[i];
        const {itemEl} = createTodoElement(item);

        list.append(itemEl);
    }
}

const searchInput = document.getElementById('search-input');
searchInput.addEventListener('input',filterTodos);

//검색버튼
function filterTodos() {
    const searchText = searchInput.value.toLowerCase();
    const filteredTodos = todos.filter(todo => 
        todo.text.toLowerCase().includes(searchText) // 검색어 포함 여부 확인
    );

    // 화면 업데이트
    list.innerHTML = ''; // 기존 리스트 초기화
    filteredTodos.forEach(item => {
        const { itemEl } = createTodoElement(item);
        list.append(itemEl); // 필터된 항목만 화면에 표시
    })

}

displayTodos();