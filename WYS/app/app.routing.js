"use strict";
var router_1 = require('@angular/router');
var personnel_component_1 = require('./modules/personnel/personnel.component');
var personnel_routing_1 = require('./modules/personnel/personnel.routing');
var appRoutes = [
    {
        path: 'personnel',
        component: personnel_component_1.PersonnelComponent,
        children: personnel_routing_1.personnelRouting,
    },
    {
        path: '',
        redirectTo: 'personnel',
        pathMatch: 'full'
    },
];
exports.routing = router_1.RouterModule.forRoot(appRoutes);
//# sourceMappingURL=app.routing.js.map