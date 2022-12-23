import React from 'react'

class BookForm extends React.Component {
    constructor(props) {
        super(props)
        this.state = {name: '', author: props.authors[0]?.uid}    // [0] - надо. ? - оператор опциональной
        // последовательности. без него не взлетит
    }

    handleChange(event) {
        this.setState(
            {
                [event.target.name]: event.target.value
            }
        );
    }

    handleSubmit(event) {
        this.props.createBook(this.state.name, this.state.author)
        // console.log(this.state.name)
        // console.log(this.state.author)
        event.preventDefault()
    }

    render() {
        return (
            <form onSubmit={(event) => this.handleSubmit(event)}>
                <div className="form-group">
                    <label for="login">name</label>
                    <input type="text" className="form-control" name="name"
                           value={this.state.name} onChange={(event) => this.handleChange(event)}/>
                </div>
                <div className="form-group">
                    <label for="author">author</label>
                    {/*<input type="number" className="form-control" name="author"*/}
                    {/*       value={this.state.authors} onChange={(event) => this.handleChange(event)}/>*/}
                    <select name="author" className='form-control' onChange={(event) => this.handleChange(event)}>
                        {this.props.authors.map((item) =>
                            <option value={item.uid}>{item.last_name} {item.first_name}
                            </option>)}
                    </select>
                </div>
                <input type="submit" className="btn btn-primary" value="Save"/>
            </form>
        );
    }
}

export default BookForm