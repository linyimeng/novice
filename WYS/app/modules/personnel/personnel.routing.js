"use strict";
var router_1 = require('@angular/router');
var department_component_1 = require('./department.component');
var staff_component_1 = require('./staff.component');
var staffcreat_component_1 = require('./staffcreat/staffcreat.component');
var staffcontent_component_1 = require('./staffcontent/staffcontent.component');
exports.PersonnelRouting = router_1.RouterModule.forRoot([
    {
        path: '',
        redirectTo: 'department',
        pathMatch: 'full'
    },
    {
        path: 'department',
        component: department_component_1.DepartmentComponent
    },
    {
        path: 'staff',
        component: staff_component_1.StaffComponent,
        children: [
            {
                path: '',
                component: staffcontent_component_1.StaffcontentComponent
            },
            {
                path: "create",
                component: staffcreat_component_1.StaffcreatComponent
            },
            {
                path: 'list',
                component: staffcontent_component_1.StaffcontentComponent
            },
        ]
    },
]);
//# sourceMappingURL=personnel.routing.js.map