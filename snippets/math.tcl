# Define some math procedures to make TCL less awful.
# Owain Kenway, 8/October/2018
proc + {a args} {
	set ret_val $a
	foreach item $args {
		set ret_val [expr $ret_val + $item]
	}
	return $ret_val
}
proc - {a args} {
	set ret_val $a
	foreach item $args {
		set ret_val [expr $ret_val - $item]
	}
	return $ret_val
}
proc * {a args} {
	set ret_val $a
	foreach item $args {
		set ret_val [expr $ret_val * $item]
	}
	return $ret_val
}

proc / {a args} {
	set ret_val $a
	foreach item $args {
		set ret_val [expr $ret_val / $item]
	}
	return $ret_val
}
