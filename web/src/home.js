import React, { Component } from 'react';
import {Carousel} from 'antd'
import img1 from './assets/img1.jpg'
import img2 from './assets/img2.jpg'
import styles from './home.module.css'

const pictures = [
	{
	  title: "标题",
	  content: "内容内容内容内容内容内容内容",
	  image: img1
	},
	{
	  title: "标题",
	  content: "内容内容内容内容内容内容内容",
	  image: img2
	},
  ];

class Home extends Component{
	render(){
		return (
			
				<Carousel autoplay effect="fade">
				{pictures.map(news => (
					<div key={news.title} className={styles.container}>
					<div className={styles.background}> <img className={styles.background_img} src={news.image} alt={news.title} /> </div>
					<div className={styles.center}>
						<img className={styles.image} src={news.image} alt={news.title} />
					</div>
					<div className={styles.description}>
						<h2>{news.title}</h2>
						<p>{news.content}</p>
					</div>
					</div>
				))}
				</Carousel>
		)
	}
}

export default Home