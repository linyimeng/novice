"use strict";
var department_right_component_1 = require('./department-right/department-right.component');
var staff_right_component_1 = require('./staff-right/staff-right.component');
var staffcreat_component_1 = require('./staffcreat/staffcreat.component');
var staffcontent_component_1 = require('./staffcontent/staffcontent.component');
exports.personnelRouting = [
    {
        path: '',
        redirectTo: 'department',
        pathMatch: 'full'
    },
    {
        path: 'department',
        component: department_right_component_1.DepartmentrightComponent
    },
    {
        path: 'staff',
        component: staff_right_component_1.StaffrightComponent,
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
];
//# sourceMappingURL=personnel.routing.js.map