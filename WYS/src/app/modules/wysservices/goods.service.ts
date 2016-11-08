import { Injectable } from '@angular/core';
import { BaseService } from './base.service';
import { Http } from '@angular/http';
@Injectable()
export class GoodsService extends BaseService {

    protected get_url = '/api/goods/goods.json';
    protected retrieve_url = '/api/goods/goods/';
    protected post_url = '/api/goods/goods.json';

    private GET_Goods_TYPE_URL = '/api/goods/type.json';

    constructor(
        http:Http
    ) { super(http); }
    
    /** 商品类型 */
    public get_goods_type() {
        return this.http.get(this.get_requesr_url(this.GET_Goods_TYPE_URL),this.get_auth_header())
                        .map(this.extractData)
                        .catch(this.httpError);
    }

    public search(keyword:string) {
        let url = this.get_requesr_url('/api/goods/search.json?search=') + keyword;
        return this.http.get(url,this.get_auth_header())
                        .map(this.extractData)
                        .catch(this.httpError);
    }

    public get_wms_goods(){
        let url = this.get_requesr_url('/api/wms/goods') + '.json';
        return this.http.get(url,this.get_auth_header())
                        .map(this.extractData)
                        .catch(this.httpError);
    }
}