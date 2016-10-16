"use strict";
var router_1 = require('@angular/router');
var department_component_1 = require('./department.component');
var staff_component_1 = require('./staff.component');
var appRoutes = [
    {
        path: 'department',
        component: department_component_1.DepartmentComponent
    },
    {
        path: '',
        redirectTo: 'department',
        pathMatch: 'full'
    },
    {
        path: 'staff',
        component: staff_component_1.StaffComponent
    },
];
exports.PersonnelRouting = router_1.RouterModule.forRoot(appRoutes);
//# sourceMappingURL=personnel.routing.js.map