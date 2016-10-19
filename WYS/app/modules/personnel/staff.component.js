"use strict";
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
var core_1 = require('@angular/core');
var StaffComponent = (function () {
    function StaffComponent() {
    }
    StaffComponent = __decorate([
        core_1.Component({
            moduleId: module.id,
            selector: 'staff',
            template: "\n    <div class=\"main\">\n\t\t<div class=\"main-left\">\n\t\t\t<h1>\n\t\t\t\t<span style=\"color:rgb(164,74,140)\">s</span>c\n\t\t\t</h1>\n\t\t\t<div class=\"list\">\n\t\t\t\t<div class=\"ultitle\" style=\"cursor: pointer;\" routerLink='/department'>\u90E8\u95E8</div>\n\t\t\t\t<div class=\"ultitle\" style=\"cursor: pointer;\" routerLink='/staff'>\u5458\u5DE5</div>\n\t\t\t</div>\n\t\t\t<div class=\"footer\">\u6B22\u8FCE\u4F7F\u7528</div>\n\t\t</div>\n\t\t<div class=\"main-right\" >\n\t\t\t<router-outlet></router-outlet>\n\t\t</div>\n    </div>\n    "
        }), 
        __metadata('design:paramtypes', [])
    ], StaffComponent);
    return StaffComponent;
}());
exports.StaffComponent = StaffComponent;
//# sourceMappingURL=staff.component.js.map