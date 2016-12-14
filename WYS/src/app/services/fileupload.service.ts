import { Injectable } from '@angular/core';
import { BaseService } from './base.service';
import { Http,Headers,RequestOptions,Response } from '@angular/http';

@Injectable()
export class FileUploadService extends BaseService {
    protected upload_img_url = '/api/fileupload/image.json';

    constructor(
        http:Http
    ) { super(http); }
    
    /**
     * 获取可用的http请求头
     */
    protected get_auth_header():RequestOptions {
        let wystoken = sessionStorage.getItem('wystoken');
        let auth_token = 'Token ' + wystoken;
        let headers = new Headers({'Authorization':auth_token});
        let options = new RequestOptions({ headers: headers });
        return options;
    }
    
    /** 上传图片 */
    uploadimg(formdata){
        return this.http.post(this.get_requesr_url(this.upload_img_url),formdata,this.get_auth_header())
                        .map(this.extractData)
                        .catch(this.httpError);
    }
}