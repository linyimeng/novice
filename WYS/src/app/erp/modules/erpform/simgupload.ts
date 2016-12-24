import { Component,OnInit,Input,Output,EventEmitter } from '@angular/core';
import { FileUploadService } from '../../../services/fileupload.service';
@Component({
   selector: 'imgupload',
   template: `
            <input type="file" #image (change)="upload_img(image)" value="上传图像">
   `,
   providers:[ FileUploadService ]
})
export class SImgUploadComponent implements OnInit{
    @Output() imgurl = new EventEmitter<string>();
    @Input() type:any;
    creator:number;

    constructor(
        private imgupload:FileUploadService
    ){ }
    
    ngOnInit(){
        let uid = sessionStorage.getItem('user');
        this.creator = Number(uid);
    }

    upload_img(input) {
        let img = input.files[0];
        let formdata = new FormData();
        formdata.append("img",img);
        formdata.append('type',this.type);
        formdata.append('creator',this.creator);
        this.imgupload.uploadimg(formdata).subscribe(
            img=>{
                /** 广播图片地址 */
                this.imgurl.emit(img.img);
            },
            error=>alert(error)
        )
    }
}

