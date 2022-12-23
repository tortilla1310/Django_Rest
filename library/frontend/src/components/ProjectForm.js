import React from 'react'

class ProjectForm extends React.Component {
    constructor(props) {
        super(props)
        this.state = {name: '', user: props.users[0]?.uid}    // [0] - надо. ? - оператор опциональной
        // последовательности. Без него не взлетит
    }

    handleChange(event) {
        this.setState(
            {
                [event.target.name]: event.target.value
            }
        );
    }

    handleSubmit(event) {
        this.props.createProject(this.state.name, this.state.user)
        // console.log(this.state.name)
        // console.log(this.state.user)
        event.preventDefault()
    }

    render() {
        return (
            <form onSubmit={(event) => this.handleSubmit(event)}>
                <div className="form-group">
                    <label form="name">Имя проекта</label>
                    <input type="text" className="form-control" name="name"
                           value={this.state.name} onChange={(event) => this.handleChange(event)}/>
                </div>
                <div className="form-group">
                    <label form="user">user</label>
                    {/*<input type="number" className="form-control" name="author"*/}
                    {/*       value={this.state.authors} onChange={(event) => this.handleChange(event)}/>*/}
                    <select name="user" className='form-control' onChange={(event) => this.handleChange(event)}>
                        {this.props.users.map((item) =>
                            <option value={item.uid}>
                                {item.username}
                            </option>)}
                    </select>
                </div>
                <input type="submit" className="btn btn-primary" value="Save"/>
            </form>
        );
    }
}

export default ProjectForm
