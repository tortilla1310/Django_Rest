import React from 'react'
import {Link} from "react-router-dom";

const BookItem = ({book, deleteBook}) => {
    return (
        <tr align="left">
            <td>
                {book.id}
            </td>
            <td>
                {book.name}
            </td>
            <td>
                {book.authors[0]?.last_name} {book.authors[0]?.first_name}
            </td>
            <td>
                <button onClick={()=>deleteBook(book.id)} type={"button"}>
                    Delete
                </button>
            </td>
        </tr>
    )
}

const BookList = ({books, deleteBook}) => {
    return (
        <div>
            <table cellSpacing="8">
                <th align="left">
                    ID
                </th>
                <th align="left">
                    Название книги
                </th>
                <th align="left">
                    Имя автора
                </th>
                {books.map((book) => <BookItem book={book} deleteBook={deleteBook} />)}
            </table>
            <Link to='/books/create'>Создать книгу</Link>
        </div>
    )
}

export default BookList