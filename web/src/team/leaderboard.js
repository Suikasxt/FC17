import '../config';
import { Link } from 'react-router-dom';
import $ from 'jquery';
import React, { Component } from 'react';
import { Table, Tabs } from 'antd';
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
		title: 'Score',
		dataIndex: 'score',
		key: 'score',
	},
	{
		title: 'AI',
		dataIndex: 'ai',
		key: 'ai',
		render: (text, record) => (
			<span>
				{record.ai?(
					<a href={global.constants.server + record.ai}>Download</a>
				) : (
					<span>None</span>
				)}
			</span>
		)
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
				for(let index in result) {
					result[index].key = index.toString();
				}
				this.setState({total : result});
			}.bind(this)
		})
		url = global.constants.server + 'api/team/leaderboard/daily';
		this.teamListRequest = $.get({
			url: url,
			success: function (result) {
				for(let index in result) {
					result[index].key = index.toString();
				}
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
