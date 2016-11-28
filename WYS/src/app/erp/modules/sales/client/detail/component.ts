import { Component,OnInit} from '@angular/core';
import { Router,ActivatedRoute } from '@angular/router';
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
   selector: 'client-detail',
   templateUrl: 'detail.html',
   providers:[CompanyService]
})
export class ClientDetailComponent{
    client:Client = new Client(null,null,true,null,null,null,null,null,null);
    constructor(
        private _clientService:CompanyService,
        private router:Router,
        private activatedRoute:ActivatedRoute
    ){}
    ngOnInit(){
        this.activatedRoute.params.forEach(
            params=>{
                let pk = +params['pk'];
                this._clientService.get_company_detail(pk).subscribe(
                    client=>this.client=client,
                    error=>alert(error)
                );
            }
        );
    }
    save_goods(){
        let json = JSON.stringify(this.client);
        let pk = this.client.pk;
        this._clientService.put_update_company(pk,json).subscribe(
            client=>{
                console.log(client);
                this.router.navigate(['sales/client/list']);
            },
            error=>alert(error)
        );
    }
}

