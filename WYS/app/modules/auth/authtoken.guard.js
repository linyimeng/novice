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
var router_1 = require('@angular/router');
/**
 * 验证token是否存在
 */
var AuthTokenGuard = (function () {
    function AuthTokenGuard(router) {
        this.router = router;
    }
    AuthTokenGuard.prototype.canActivate = function () {
        var token = localStorage.getItem('wystoken');
        if (token) {
            return true;
        }
        else {
            //this.router.navigate([LoginComponent]);
            return true;
        }
    };
    AuthTokenGuard = __decorate([
        core_1.Injectable(), 
        __metadata('design:paramtypes', [router_1.Router])
    ], AuthTokenGuard);
    return AuthTokenGuard;
}());
exports.AuthTokenGuard = AuthTokenGuard;
//# sourceMappingURL=authtoken.guard.js.map