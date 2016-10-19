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
var common_1 = require('@angular/common');
var router_1 = require('@angular/router');
var personnel_component_1 = require('./personnel.component');
var department_right_component_1 = require('./department-right/department-right.component');
var departmentcontent_component_1 = require('./departmentcontent/departmentcontent.component');
var staffcreat_component_1 = require('./staffcreat/staffcreat.component');
var staffdetail_component_1 = require('./staffdetail/staffdetail.component');
var staff_right_component_1 = require('./staff-right/staff-right.component');
var staffcontent_component_1 = require('./staffcontent/staffcontent.component');
var authtoken_guard_1 = require('../auth/authtoken.guard');
var PersonnelModule = (function () {
    function PersonnelModule() {
    }
    PersonnelModule = __decorate([
        core_1.NgModule({
            imports: [
                common_1.CommonModule,
                router_1.RouterModule,
            ],
            declarations: [
                personnel_component_1.PersonnelComponent,
                department_right_component_1.DepartmentrightComponent,
                departmentcontent_component_1.DepartmentcontentComponent,
                staffcontent_component_1.StaffcontentComponent,
                staffcreat_component_1.StaffcreatComponent,
                staffdetail_component_1.StaffdetailComponent,
                staffcreat_component_1.StaffcreatComponent,
                staff_right_component_1.StaffrightComponent,
            ],
            exports: [],
            providers: [
                authtoken_guard_1.AuthTokenGuard,
            ]
        }), 
        __metadata('design:paramtypes', [])
    ], PersonnelModule);
    return PersonnelModule;
}());
exports.PersonnelModule = PersonnelModule;
//# sourceMappingURL=personnel.module.js.map