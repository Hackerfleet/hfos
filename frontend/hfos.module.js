/*
 * HFOS - Hackerfleet Operating System
 * ===================================
 * Copyright (C) 2011-2019 Heiko 'riot' Weinen <riot@c-base.org> and others.
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Affero General Public License as
 * published by the Free Software Foundation, either version 3 of the
 * License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU Affero General Public License for more details.
 *
 * You should have received a copy of the GNU Affero General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */

import './hfos-design.scss';

import angular from 'angular';

export default angular
    .module('main.app.hfos', [])
    .run(function (user) {
        user.logo_url = '/src/components/hfos/assets/hackerfleet.svg';
        user.menu_icon_url = '/src/components/hfos/assets/hackerfleet32.svg';
    })
    .name;