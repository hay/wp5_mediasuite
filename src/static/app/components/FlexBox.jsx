import React from 'react';

class FlexBox extends React.Component {
	constructor(props) {
		super(props);
		this.state = {
			visible: true
		}
	}

	toggle() {
		this.setState({
			visible: !this.state.visible
		});
	}

	render() {
		return (
			<div className="well">
				<div className="text-right">
					<i className={this.state.visible ? 'glyphicon glyphicon-menu-down' : 'glyphicon glyphicon-menu-up'}
						onClick={this.toggle.bind(this)}></i>
				</div>
				{this.state.visible ? this.props.children : ''}
			</div>
		)
	}
}

export default FlexBox;