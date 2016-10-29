import { Injectable } from '@angular/core';
import { BaseService } from './base.service';
import { Http,Headers,RequestOptions } from '@angular/http';

@Injectable()
export class GoodsService extends BaseService {
    private GET_Goods_LIST_URL = '/api/goods/goods.json';
    private GET_Goods_DETAIL_URL = '/api/goods/goods/';
    private POST_Goods_CREATE_URL = '/api/goods/goods.json';

    constructor(
        http:Http
    ) { super(http); }

    /** 获取商品列表 */
    get_goods_list() {
        return this.http.get(this.get_requesr_url(this.GET_Goods_LIST_URL),this.get_auth_header())
                 .map(this.extractData)
                 .catch(this.httpError);
    }

    /** 获取单个商品 */
    get_goods_detail(pk:number) {
        let detailUrl = this.get_requesr_url(this.GET_Goods_DETAIL_URL) + String(pk) + '.json';
        console.log(detailUrl);
        return this.http.get(detailUrl,this.get_auth_header())
                        .map(this.extractData)
                        .catch(this.httpError);
    }

    /** 创建商品 */
    post_create_goods(json:string) {
        return this.http.post(this.get_requesr_url(this.POST_Goods_CREATE_URL),json,this.get_auth_header())
                        .map(this.extractData)
                        .catch(this.httpError);
    }

    /** 更新一整个商品put */
    put_update_goods(pk,json:string) {
        let updateUrl = this.get_requesr_url(this.GET_Goods_DETAIL_URL) + String(pk) + '.json';
        return this.http.put(updateUrl,json,this.get_auth_header())
                        .map(this.extractData)
                        .catch(this.httpError);
    }
}