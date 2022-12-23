import React from 'react'
import {Link} from 'react-router-dom'

const AuthorItem = ({author}) => {
    return (
        <tr align="left">
            <td>
                <Link to={`author/${author.uid}`}> {author.uid} </Link>
            </td>
            <td>
                {author.last_name} {author.first_name}
            </td>
            <td>
                {author.birthday_year}
            </td>
        </tr>
    )
}

const AuthorList = ({authors}) => {
    return (
        <table cellSpacing="8">
            <th align="left">
                UID
            </th>
            <th align="left">
                Имя
            </th>
            <th align="left">
                Дата рождения
            </th>
            {authors.map((author) => <AuthorItem author={author}/>)}
        </table>
    )
}

export default AuthorList