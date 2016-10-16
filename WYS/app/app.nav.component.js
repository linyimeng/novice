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
var NavComponent = (function () {
    function NavComponent() {
    }
    NavComponent = __decorate([
        core_1.Component({
            moduleId: module.id,
            selector: 'wys-nav',
            template: "\n        <nav>\n            <ul>\n                <li routerLink=\"/yg\" routerLinkActive=\"activity\" class=\"activity\">\n                    <a routerLink='/department'>\u5458\u5DE5</a>\n                </li>\n                <li routerLink=\"/jh\">\n                    <a href=\"#\">\u8FDB\u8D27</a>\n                </li>\n                <li routerLink=\"/xs\">\n                    <a href=\"#\">\u9500\u552E</a>\n                </li>\n                <li routerLink=\"/ck\">\n                    <a href=\"#\">\u4ED3\u5E93</a>\n                </li>\n                <li routerLink=\"/cw\">\n                    <a href=\"#\">\u8D22\u52A1</a>\n                </li>\n                <li routerLink=\"/sz\">\n                    <a href=\"#\">\u8BBE\u7F6E</a>\n                </li>\n            </ul>\n            <div class=\"nav-left\">\n                <span class=\"iconfont\">&#xe647;</span>\n                <div class=\"user-div\">\n                    <span class=\"iconfont\">&#xe621;</span>\n                    <span class=\"user\">admin</span>\n                    <span class=\"iconfont triangle\">&#xe696;</span>\n                </div>\n            </div>\n        </nav>\n    "
        }), 
        __metadata('design:paramtypes', [])
    ], NavComponent);
    return NavComponent;
}());
exports.NavComponent = NavComponent;
//# sourceMappingURL=app.nav.component.js.map