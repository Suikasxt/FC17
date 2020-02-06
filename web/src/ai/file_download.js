import React, {Component } from 'react';

class File_download extends Component{
    render(){
        let url = global.constants.server + 'api/ai/download/'+this.props.match.params.pk+'/';
        console.log('file download')
        return(
            <div style={{display: 'none'}}>
                <iframe src={url} title='download file'/>
            </div>
        )
    }
}

export default File_download;