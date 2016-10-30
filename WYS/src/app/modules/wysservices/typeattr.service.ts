import { Injectable } from '@angular/core';
import { BaseService } from './base.service';
import { Http,Headers,RequestOptions } from '@angular/http';

@Injectable()
export class TypeattrService extends BaseService {
    private GET_ATTR_LIST_URL = '/api/goods/typeattr/';

    constructor(
        http:Http
    ) { super(http); }

    /** 获取单个类别的静态属性 */
    get_attr_list(attr_type:string,goodstype:number) {
        let AttrTypeUrl = this.get_requesr_url(this.GET_ATTR_LIST_URL) + attr_type + '/'+goodstype + '.json';
        console.log(AttrTypeUrl);
        return this.http.get(AttrTypeUrl,this.get_auth_header())
                        .map(this.extractData)
                        .catch(this.httpError);
    }
}