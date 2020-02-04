import '../config';
import { withRouter, Link } from 'react-router-dom';
import $ from 'jquery';
import React, { Component } from 'react';
import { Table, Divider, Tabs } from 'antd';
const { TabPane } = Tabs;

const columns = [
	{
		title: 'Rank',
		dataIndex: 'rank',
		key: 'rank',
	},
	{
		title: 'Name',
		dataIndex: 'name',
		key: 'name',
		render: (text, record) => <Link to={"team/detail/" + record.id}>{text}</Link>,
	},
	{
		title: 'Introduction',
		dataIndex: 'introduction',
		key: 'introduction',
	},
	{
		title: 'score',
		dataIndex: 'score',
		key: 'score',
	},
];

class Leaderboard extends Component{
	state = {
		total : [],
		daily : [],
	}
	getTeamList = () => {
		let url = global.constants.server + 'api/team/leaderboard/total';
		this.teamListRequest = $.get({
			url: url,
			success: function (result) {
				this.setState({total : result});
			}.bind(this)
		})
		url = global.constants.server + 'api/team/leaderboard/daily';
		this.teamListRequest = $.get({
			url: url,
			success: function (result) {
				this.setState({daily : result});
			}.bind(this)
		})
	}
	componentWillMount(){
		this.getTeamList();
	}
	render(){
		return (
			<div  id = "root">
				<Tabs defaultActiveKey="1">
					<TabPane tab="Total" key="total">
						<Table columns={columns} dataSource={this.state.total} />
					</TabPane>
					<TabPane tab="Daily" key="daily">
						<Table columns={columns} dataSource={this.state.daily} />
					</TabPane>
				</Tabs>
			</div>
		)
	}
}
export default Leaderboard;
