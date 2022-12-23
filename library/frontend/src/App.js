import React from 'react';
// import logo from './logo.svg';
import './App.css';
// import UserList from "./components/User";
import axios from "axios";
// import MenuList from "./components/Menu";
// import FooterList from "./components/Footer";
import AuthorList from "./components/Author";
import {Route, Link, Switch, Redirect, BrowserRouter} from 'react-router-dom';
// import AuthorBookList from "./components/AuthorBook";
import ErrorLogo from './images/Bobby_Chiu.jpg';
import UserList from "./components/User";
import ProjectList from "./components/Projects";
import ToDosList from "./components/ToDos";
import LoginForm from "./components/Auth";
import Cookies from 'universal-cookie';
import BookList from "./components/books";
import AuthorBookList from "./components/AuthorBook";
import BookForm from "./components/BookForm";
import ProjectForm from "./components/ProjectForm";
import ToDoForm from "./components/ToDoForm";


const NotFound404 = ({location}) => {
    return (
        <div>
            <div>
                <img src={ErrorLogo}
                     alt={'отчаяние'} width="450" height="300"></img>
            </div>
            <div>
                <h1>"Страница по адресу '{location.pathname}' не найдена"</h1>
            </div>
        </div>
    )
}

class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'authors': [],
            'books': [],
            'users': [],
            'projects': [],
            'ToDos': [],
            'token': '',
        }
    }

    set_token(token) {
        const cookies = new Cookies()
        cookies.set('token', token)
        this.setState({'token': token}, () => this.load_data())
    }

    is_authenticated() {
        return this.state.token !== ''
    }

    logout() {
        this.set_token('')
    }

    get_token_from_storage() {
        const cookies = new Cookies()
        const token = cookies.get('token')
        this.setState({'token': token}, () => this.load_data())
    }

    get_token(username, password) {
        axios.post('http://127.0.0.1:8000/api-token-auth/', {
            username: username,
            password: password
        })
            .then(response => {
                this.set_token(response.data['token'])
            }).catch(error => alert('Неверный логин или пароль'))
    }

    get_headers() {
        let headers = {
            'Content-Type': 'application/json'
        }
        if (this.is_authenticated()) {
            headers['Authorization'] = 'Token ' + this.state.token
        }
        return headers
    }

    load_data() {
        const headers = this.get_headers()
        axios.get('http://127.0.0.1:8000/api/users/')
            .then(response => {
                const users = response.data
                this.setState(
                    {
                        'users': users
                    }
                )
            }).catch(error => console.log(error));

        axios.get('http://127.0.0.1:8000/filters/project/')
            .then(response => {
                const projects = response.data
                this.setState(
                    {
                        'projects': projects
                    }
                )
            }).catch(error => console.log(error));

        axios.get('http://127.0.0.1:8000/api/todo/')
            .then(response => {
                const ToDos = response.data
                this.setState(
                    {
                        'ToDos': ToDos
                    }
                )
            }).catch(error => console.log(error));

        axios.get('http://127.0.0.1:8000/api/authors/', {headers})
            .then(response => {
                this.setState({authors: response.data})
            }).catch(error => console.log(error));

        axios.get('http://127.0.0.1:8000/api/books/', {headers})
            .then(response => {
                this.setState({books: response.data})
            }).catch(error => {
            console.log(error)
            this.setState({books: []});
        })
    }

    deleteBook(id) {
        const headers = this.get_headers()
        axios.delete(`http://127.0.0.1:8000/api/books/${id}`, {headers})
            .then(response => {
                this.setState({
                    books: this.state.books.filter((books) => books.id !== id)
                })
            }).catch(error => console.log(error))
    }

    createBook(name, author) {
        const headers = this.get_headers()
        const data = {name: name, authors: [author]}
        // console.log("вот и переменная", data)
        axios.post(`http://127.0.0.1:8000/api/books/`, data, {headers})
            .then(response => {
                let new_book = response.data
                new_book.author = this.state.authors.filter((item) => item.uid === new_book.author)[0]
                this.setState({books: [...this.state.books, new_book]})
            }).catch(error => console.log(error))
    }

    createProject(name, user) {
        const headers = this.get_headers()
        const data = {name_project: name, users: [user]}
        // console.log("вот и переменная", data)
        axios.post(`http://127.0.0.1:8000/api/project/`, data, {headers})
            .then(response => {
                let new_project = response.data
                new_project.user = this.state.users.filter((item) => item.uid === new_project.user)[1]
                this.setState({projects: [...this.state.projects, new_project]})
            }).catch(error => console.log(error))
    }

    deleteProject(uid) {
        const headers = this.get_headers()
        axios.delete(`http://127.0.0.1:8000/api/project/${uid}`, {headers})
            .then(response => {
                this.setState({
                    projects: this.state.projects.filter((projects) => projects.uid !== uid)
                })
            }).catch(error => console.log(error))
    }

    createTodo(name, created_by, project) {
        const headers = this.get_headers()
        const data = {text: name, created_by: created_by, project: project}
        // console.log("вот и переменная", data)
        axios.post(`http://127.0.0.1:8000/api/todo/`, data, {headers})
            .then(response => {
                let new_ToDos = response.data
                new_ToDos.project = this.state.projects.filter((item) => item.uid === new_ToDos.project)[0]
                this.setState({ToDos: [...this.state.ToDos, new_ToDos]})
            }).catch(error => console.log(error))
    }

    deleteTodo(uid) {
        const headers = this.get_headers()
        axios.delete(`http://127.0.0.1:8000/api/todo/${uid}`, {headers})
            .then(response => {
                this.setState({
                    projects: this.state.projects.filter((projects) => projects.uid !== uid)
                })
            }).catch(error => console.log(error))
    }

    searchProject(name_project) {
        const headers = this.get_headers()
        console.log('странный список', name_project)
        axios.get(`http://127.0.0.1:8000/api/project/`, {headers})
            .then(response => {
                this.setState({
                    projects: this.state.projects.filter((item) => item.name_project.toLowerCase().includes(name_project))
                })
            }).catch(error => console.log(error))
    }

    // projects: this.state.projects.filter((item) => item.name_project.toLowerCase() === name_project.toLowerCase())

    componentDidMount() {
        this.get_token_from_storage()
        this.load_data()
    }

    render() {
        return (
            <div className="App">
                <BrowserRouter>
                    <nav>
                        <ul>
                            <li>
                                <Link to='/'>Authors</Link>
                            </li>
                            <li>
                                <Link to='/books'>Books</Link>
                            </li>
                            <li>
                                <Link to='/users'>Users</Link>
                            </li>
                            <li>
                                <Link to='/projects'>Projects</Link>
                            </li>
                            <li>
                                <Link to='/ToDos'>ToDos</Link>
                            </li>
                            <li>
                                {this.is_authenticated() ? <button
                                    onClick={() => this.logout()}>Logout</button> : <Link to='/login'>Login</Link>}
                            </li>
                        </ul>
                    </nav>
                    <Switch>
                        <Route exact path='/' component={() => <AuthorList authors={this.state.authors}/>}/>
                        <Route exact path='/books' component={() => <BookList books={this.state.books}
                                                                              deleteBook={(id) =>
                                                                                  this.deleteBook(id)}/>}/>
                        <Route exact path='/books/create' component={() => <BookForm authors={this.state.authors}
                                                                                     createBook={(name, author) =>
                                                                                         this.createBook(name, author)}/>}/>

                        <Route exact path="/author/:uid" component={() => <AuthorBookList items={this.state.books}/>}/>

                        <Route exact path='/login' component={() => <LoginForm
                            get_token={(username, password) => this.get_token(username, password)}/>}/>

                        <Route exact path='/users' component={() => <UserList users={this.state.users}/>}/>


                        <Route exact path='/ToDos' component={() => <ToDosList ToDos={this.state.ToDos}
                                                                               users={this.state.users}
                                                                               deleteTodo={(uid) =>
                                                                                   this.deleteTodo(uid)}/>}/>
                        <Route exact path='/ToDos/create' component={() =>
                            <ToDoForm projects={this.state.projects}
                                      users={this.state.users}
                                      createTodo={(name, created_by, project) =>
                                          this.createTodo(name, created_by, project)}/>}/>

                        <Route exact path='/projects' component={() => <ProjectList projects={this.state.projects}
                                                                                    users={this.state.users}
                                                                                    deleteProject={(uid) =>
                                                                                        this.deleteProject(uid)}
                                                                                    searchProject={(name_project) =>
                                                                                        this.searchProject(name_project)}/>}/>
                        <Route exact path='/projects/create' component={() =>
                            <ProjectForm users={this.state.users}
                                         createProject={(name, user) => this.createProject(name, user)}/>}/>

                        <Route exact path='/login' component={() => <LoginForm
                            get_token={(username, password) => this.get_token(username, password)}/>}/>

                        <Redirect from='/authors' to='/'/>
                        <Route component={NotFound404}/>
                    </Switch>
                </BrowserRouter>
            </div>
        )
    }
}

export default App;
