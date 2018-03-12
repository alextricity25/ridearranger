import re
import pdb

class LineParser():

    '''
    This class parses the request made by a user via GroupMe
    into a result dataset containing the following properties:
    * modifiers (any words preceeded with '-', '+', or '~'
        * Excluded - any people that are excluded
        * Included - any people that are included
        * Role removal - Any people that have had a role modified
                         i.e. the driver role has been removed
    * Scenario rules (any words preceeded with '$'
    '''
    def __init__(self, line):
        self.line = line
        self.result = {
            "modifiers": {
                "excluded": [],
                "included": [],
                "role_removal": []
             },
             "scenario_rule": ""
        }

    def get_result(self):
        modifier_reg = re.compile('[-+~][A-Za-z]+')
        scenario_reg = re.compile('\$[-_A-Za-z0-9]+')
        modifiers = modifier_reg.findall(self.line)
        scenario = scenario_reg.findall(self.line)
        self._build_modifiers(modifiers)
        # If no scenario is given, use the default scenario
        if not scenario:
            self.result['scenario_rule'] = "Default"
        else:
            self.result['scenario_rule'] = scenario[0][1:]
        return self.result

    def _build_modifiers(self, modifiers):
        excluded_mods = []
        included_mods = []
        role_rem_mods = []
        for mod in modifiers:
            if mod[0] == '-':
                excluded_mods.append(mod)
            elif mod[0] == '+':
                included_mods.append(mod)
            elif mod[0] == '~':
                role_rem_mods.append(mod)
        self.result['modifiers']['excluded'] = excluded_mods
        self.result['modifiers']['included'] = included_mods
        self.result['modifiers']['role_removal'] = role_rem_mods
