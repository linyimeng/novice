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
var DepartmentComponent = (function () {
    function DepartmentComponent() {
    }
    DepartmentComponent = __decorate([
        core_1.Component({
            moduleId: module.id,
            selector: 'department',
            template: "\n    <div class=\"main\">\n\t\t<!-- \u516C\u5171\u90E8\u5206\u9700\u6A21\u5757\u5316\uFF0C\u5F85\u6A21\u5757\u591A\u540E\u7EDF\u4E00\u91CD\u65B0\u8BBE\u8BA1\u4FEE\u6539 -->\n\t\t<div class=\"main-left\">\n\t\t\t<h1>\n\t\t\t\t<span style=\"color:rgb(164,74,140)\">s</span>c\n\t\t\t</h1>\n\t\t\t<div class=\"list\">\n\t\t\t\t<staff-list></staff-list>\n\t\t\t</div>\n\t\t\t<div class=\"footer\">\u6B22\u8FCE\u4F7F\u7528</div>\n\t\t</div>\n\n\t\t<div class=\"main-right\" >\n\t\t\t<div class=\"title\">\n\t\t\t\t<department-title></department-title>\n\t\t\t</div>\n\t\t\t<div class=\"content\">\n\t\t\t\t<department-content></department-content>\n\t\t\t</div>\n\t\t</div>\n    </div>\n    "
        }), 
        __metadata('design:paramtypes', [])
    ], DepartmentComponent);
    return DepartmentComponent;
}());
exports.DepartmentComponent = DepartmentComponent;
//# sourceMappingURL=department.component.js.map