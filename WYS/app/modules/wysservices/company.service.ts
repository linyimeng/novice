import { Injectable } from '@angular/core';
import { BaseService } from './base.service';
import { Http,Headers,RequestOptions } from '@angular/http';

@Injectable()
export class CompanyService extends BaseService {
    private GET_SUPPLIER_LIST_URL = '/api/bp/companytype/vendor.json';
    private GET_COMPANY_DETAIL_URL = '/api/bp/company/';
    private POST_COMPANY_CREATE_URL = '/api/bp/company.json';

    constructor(
        http:Http
    ) { super(http); }

    /** 获取供应商列表 */
    get_supplier_list() {
        return this.http.get(this.get_requesr_url(this.GET_SUPPLIER_LIST_URL),this.get_auth_header())
                 .map(this.extractData)
                 .catch(this.httpError);
    }

    /** 获取单个公司详情 */
    get_company_detail(pk:number) {
        let detailUrl = this.get_requesr_url(this.GET_COMPANY_DETAIL_URL) + String(pk) + '.json';
        console.log(detailUrl);
        return this.http.get(detailUrl,this.get_auth_header())
                        .map(this.extractData)
                        .catch(this.httpError);
    }

    /** 创建公司 */
    post_create_company(json:string) {
        return this.http.post(this.get_requesr_url(this.POST_COMPANY_CREATE_URL),json,this.get_auth_header())
                        .map(this.extractData)
                        .catch(this.httpError);
    }

    /** 更新一整个公司put */
    put_update_company(pk,json:string) {
        let updateUrl = this.get_requesr_url(this.GET_COMPANY_DETAIL_URL) + String(pk) + '.json';
        return this.http.put(updateUrl,json,this.get_auth_header())
                        .map(this.extractData)
                        .catch(this.httpError);
    }
}