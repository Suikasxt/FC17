import React, { Component } from 'react';
import {Carousel} from 'antd'
import img1 from './assets/img1.jpg'
import img2 from './assets/img2.jpg'
import img3 from './assets/img3.jpg'
import img4 from './assets/img4.jpg'
import styles from './home.module.css'


const pictures = [
	{
	  title: "",
	  content: "",
	  image: img3
	},
	{
	  title: "",
	  content: "",
	  image: img4
	},
  ];

class Home extends Component{
	render(){
		return (
			<div>
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
			</div>
		)
	}
}

export default Home