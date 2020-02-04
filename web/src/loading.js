import './config';
import { withRouter, Link } from 'react-router-dom';
import $ from 'jquery';
import React, { Component } from 'react';
import { message, Button, Card, Modal  } from 'antd';


class Loading extends Component{
	render(){
		return (
			<div  id = "root">
				Loading...
			</div>
		)
	}
}

export default Loading;