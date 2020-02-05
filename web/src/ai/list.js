import '../config';
import {List,Button} from 'grommet'
import {Upload} from "grommet-icons"
import $ from 'jquery';
import React, { Component } from 'react';
import Loading from '../loading.js'
import {location} from 'react-router'
import { Link, Route, Redirect, withRoute} from 'react-router-dom';
import { Layout } from 'antd';

class AIList extends Component{
	state = {
	}
	getAIList = () => {
		let url = global.constants.server + 'api/ai/list/';
		this.AIListRequest = $.get({
			url: url,
			success: function (result) {
				this.setState({list : result});
			}.bind(this)
		})
	}
	componentWillMount(){
		this.getAIList();
    }
	
	upload_redirect = (event) => {
		this.props.history.push("/ai/upload");
	  }

	render(){
		if (this.state.list == null){
			console.log("no list")
			return (
				<Loading></Loading>
			)
		}

		console.log(this.state.list)
        return(
			<div align="center">
			<Button icon={<Upload/>}
			history={this.props.history}
			label="Upload" onClick={this.upload_redirect}></Button>
			</div>
			)
            
    }
        
};

export default AIList;