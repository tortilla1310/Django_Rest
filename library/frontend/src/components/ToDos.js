import React from 'react'
import {Link} from "react-router-dom";

const ToDoItem = ({ToDo, deleteTodo, user}) => {
    let obj = user.find(o => o.uid === ToDo.created_by)
    console.log(ToDo.created_by)
    return (
        <tr>
            <td>
                {ToDo.update_at}
            </td>
            <td>
                {obj.username}
            </td><br></br>
            <td>
                {ToDo.text}
            </td>
            <td>
                <button onClick={()=>deleteTodo(ToDo.uid)} type={"button"}>
                    Delete
                </button>
            </td>
        </tr>
    )
}

const ToDosList = ({ToDos, deleteTodo, users}) => {
    return (
        <div>
            <table>
                <th>
                    Дата создания
                </th>
                <th>
                    Имя создателя
                </th><br></br>
                <th>
                    Текст
                </th>
                {ToDos.map((ToDo) => <ToDoItem ToDo={ToDo} deleteTodo={deleteTodo} user={users}/>)}
            </table>
            <Link to='/ToDos/create'>Создать проект</Link>
    </div>
    )
}

export default ToDosList