const addButton = document.getElementById("add-todo");
const viewOption = document.getElementById("view");
const sortOption = document.getElementById("sort");

const InProgress = document.getElementById("ing");
const Completed = document.getElementById("completed")

addButton.onclick = () => {
    addTodo(InProgress,1); // add=1
};
viewOption.onchange = () => {
    setTodo();
}
sortOption.onchange = () => {
    setTodo();
}


function addTodo(Parent,add = 0, id = null, title = "",date=null, rating = 0) {
    let list = localStorage.getItem('todo')
    if (add === 1) {
        console.log(add);
        if (list === null || list === "") {
            list = [];
        } else {
            list = JSON.parse(list);
        }
        // id 설정: 배열이 비어있다면 id는 1, 아니면 마지막 요소의 id 값 + 1
        id = list.length > 0 ? list[list.length - 1].id + 1 : 1;
        var today = new Date();
        // 미국시간 기준이니까 9를 더해주면 대한민국 시간됨
        today.setHours(today.getHours() + 9);
        // 문자열로 바꿔주고 T를 빈칸으로 바꿔주면 yyyy-mm-dd hh:mm:ss 이런 형식 나옴
        date =  today.toISOString().replace("T", " ").substring(0, 19);// ISO 형식 (YYYY-MM-DD)

        const todo = {
            id: id,
            title: "",
            date: date,
            rating: 0,
            state:false
        };

        list.push(todo);
        localStorage.setItem("todo", JSON.stringify(list));
    }
    list = localStorage.getItem('todo')
    list = JSON.parse(list)
    const findIndex = list.findIndex(item=>item.id==id);

    // todo-item 추가
    const todo_item = document.createElement("div");
    todo_item.className = "todo-item";
    todo_item.id = id;

    // todo-item 안에 checkbox 추가
    const todo_check = document.createElement("input");
    todo_check.type = "checkbox";
    todo_check.checked = list[findIndex].state;
    todo_check.addEventListener('change',function(){
        list[findIndex].state = todo_check.checked;
        localStorage.setItem('todo',JSON.stringify(list))
        setTodo();
    })
    const todo_header = document.createElement('div');
    todo_header.className = "todo-header"

    const todo_date = document.createElement('span');
    todo_date.textContent = date;

    // todo-item 안에 input 요소 추가
    const todo_input = document.createElement("input");
    todo_input.type = "text";
    todo_input.disabled = true;
    todo_input.id = id;
    todo_input.value = title;

    todo_input.addEventListener("blur", function () {
        //교체해주기
        if (findIndex !== -1) {
            list[findIndex].title = todo_input.value;
            localStorage.setItem('todo', JSON.stringify(list)); // JSON.stringify로 저장
        }
        todo_input.disabled = true;
    });
    todo_header.appendChild(todo_check)
    todo_header.appendChild(todo_input);

    const todo_star = document.createElement("div");
    for (let i = 1; i <= 5; i++) {
        const star = document.createElement("span");
        star.className = "star";
        star.dataset.value = i; // 각 별의 값을 설정
        star.addEventListener("click", function() {
            //평점 저장
            list[findIndex].rating = i;
            localStorage.setItem('todo',JSON.stringify(list));

            //별 표시
            const starlist = todo_star.childNodes;
            if (star.classList.contains('selected'))
            {
                for(let j=i;j<5;j++)
                {
                    starlist[j].classList.remove('selected');
                }
            }
            else
            {
                for(let j = 0;j<i;j++)
                    {
                        starlist[j].classList.add('selected');
                    }
            }
        });
        todo_star.appendChild(star);
    }
    const starlist = todo_star.childNodes;
    for(let i = 0;i<rating;i++)
    {
        starlist[i].classList.add('selected');
    }

    const control_button = document.createElement('div');
    // revise 버튼 추가
    const revise_button = document.createElement("button");
    revise_button.className="control-button"
    revise_button.textContent = "Revise";
    revise_button.onclick = function () {
        todo_input.disabled = false;
        todo_input.focus();
    };

    // delete 버튼 추가
    const delete_button = document.createElement("button");
    delete_button.className="control-button"
    delete_button.textContent = "Delete";
    delete_button.onclick = function () {
        list = list.filter(item => item.id !== id);
        document.getElementById(id).remove();
        localStorage.setItem('todo', JSON.stringify(list)); // JSON.stringify로 저장
        
    };
    control_button.appendChild(revise_button);
    control_button.appendChild(delete_button);

    // todo-item에 요소 추가
    todo_item.appendChild(todo_header);
    todo_item.appendChild(todo_star);
    todo_item.appendChild(todo_date);
    todo_item.appendChild(control_button);

    // todo-list에 todo-item 추가
    Parent.appendChild(todo_item);
}

window.onload = () => {
    setTodo();
};
const setTodo = () => {
    let list = localStorage.getItem('todo');
    if (list === null || list === "") {
        list = [];
    } else {
        list = JSON.parse(list);
        //정렬 옵션 적용하기
        const view = viewOption.value;
        const sort = +(sortOption.value);
        list.sort((a, b) => {
            if (view == "title")
                return sort * a.title.localeCompare(b.title);
            if (view === "date") {
                return sort * (new Date(a.date) - new Date(b.date)); // 날짜 비교
            }
            return sort * (a[view] - b[view]); // 숫자 속성 비교
        });
        //상태 옵션 적용하기
        const ing = list.filter(item=>item.state==false)
        const completed = list.filter(item=>item.state==true)
        InProgress.innerHTML = ""
        for (const item of ing) {
            addTodo(InProgress,0, item.id, item.title, item.date, item.rating);
        }
        Completed.innerHTML = ""
        for (const item of completed) {
            addTodo(Completed,0, item.id, item.title, item.date, item.rating);
        }
    }


}
