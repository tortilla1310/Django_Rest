import React from 'react'
import {Link} from "react-router-dom";

const ProjectItem = ({project, deleteProject, user}) => {
    let obj = user.find(o => o.uid === project.users[0])
    return (
        <tr align="left">
            <td>
                {project.uid}
            </td>
            <td>
                {project.name_project}
            </td>
            <td>
                {obj.username}
            </td>
            <td>
                <button onClick={() => deleteProject(project.uid)} type={"button"}>
                    Delete
                </button>
            </td>
        </tr>
    )
}

const ProjectList = ({projects, deleteProject, users, searchProject}) => {
    // const projSearch = ['']

    let projSearch;
    return (
        <div>
            <div className={'form'}>
                <form className={'search_form'} onSubmit="alert('submit!');return false">
                    <input
                        type='text'
                        id="input_form"
                        name="input_form"
                        placeholder='поиск пока не работает'
                        className='search_input'
                        onChange={(event) => projSearch.log(event.target.value.toLowerCase())}
                    />
                    {/*поиск пока не работает*/}
                    <button onClick={() => searchProject(projSearch)} type={"button"}>
                        Поиск
                    </button>
                </form>
            </div>


            <table cellSpacing="8">
                <th align="left">
                    UID
                </th>
                <th align="left">
                    Название проекта
                </th>
                <th align="left">
                    Имя автора
                </th>
                {projects.map((project) => <ProjectItem project={project} deleteProject={deleteProject} user={users}/>)}
            </table>
            <Link to='/projects/create'>Создать проект</Link>
        </div>
    )
}
export default ProjectList