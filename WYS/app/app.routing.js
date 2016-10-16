"use strict";
var router_1 = require('@angular/router');
var department_component_1 = require('./component/personnel/department.component');
var staff_component_1 = require('./component/personnel/staff.component');
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
exports.routing = router_1.RouterModule.forRoot(appRoutes);
//# sourceMappingURL=app.routing.js.map