import React from 'react'

class createTodo extends React.Component {
    constructor(props) {
        super(props)
        this.state = {name: '', created_by: props.users[0]?.uid, project: ''}
    }

    handleChange(event) {
        this.setState(
            {
                [event.target.name]: event.target.value
            }
        );
    }

    handleSubmit(event) {
        this.props.createTodo(this.state.name, this.state.created_by, this.state.project)
        // console.log(this.state.name)
        // console.log(this.state.created_by)
        // console.log(this.state.project)
        event.preventDefault()
    }

    render() {
        return (
            <form onSubmit={(event) => this.handleSubmit(event)}>
                <div className="form-group">
                    <label For="name"></label>
                    <input type="text" className="form-control" name="name"
                           value={this.state.name} onChange={(event) => this.handleChange(event)}/>
                </div>
                <div className="form-group">
                    <label For="created_by">Имя создателя: </label>
                    {/*<input type="number" className="form-control" name="author"*/}
                    {/*       value={this.state.authors} onChange={(event) => this.handleChange(event)}/>*/}
                    <select name="created_by" className='form-control' onChange={(event) => this.handleChange(event)}>
                        {this.props.users.map((item) =>
                            <option value={item.uid}>
                                {item.username}
                            </option>)}
                    </select>
                </div>
                <div className="form-group">
                    <label For="project">Имя проекта: </label>
                    <select name="project" className='form-control' onChange={(event) => this.handleChange(event)}>
                        {this.props.projects.map((item) =>
                            <option value={item.uid}>
                                {item.name_project}
                            </option>)}
                    </select>
                </div>
                    <input type="submit" className="btn btn-primary" value="Save"/>
            </form>
        );
    }
}

export default createTodo