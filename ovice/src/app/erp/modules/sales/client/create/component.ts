import { Component } from '@angular/core';
import { Router } from '@angular/router';

import { CompanyService } from '../../../../../services//company.service';

class Client {
    constructor(
        public pk:number,
        name:string,
        public is_client:boolean,
        landline:string,
        phone:string,
        email:string,
        fax:string,
        address:string,
        remark:string
    ){}
}
@Component({
   selector: 'client-create',
   templateUrl: 'create.html',
   providers:[CompanyService]
})
export class ClientCreateComponent {

    client:Client = new Client(null,null,true,null,null,null,null,null,null);

    constructor(
        private _supplierService:CompanyService,
        private router:Router
    ){}

    save_goods(){
        this.client.is_client = true;
        let json = JSON.stringify(this.client);
        this._supplierService.post_create_company(json).subscribe(
            client=>{
                console.log(client);
                this.router.navigate(['sales/client/list']);
            },
            error=>alert(error)
        );
    }
}
