diff --git a/z_calibration.py b/z_calibration.py
index 92f10b7..c2a6a82 100644
--- a/z_calibration.py
+++ b/z_calibration.py
@@ -323,7 +323,8 @@ class CalibrationState:
         #if probe.mcu_probe.query_endstop(time):
         #    raise self.helper.printer.command_error(ERROR_NOT_ATTACHED)
         #    return
-        switch_zero = self._probe_on_z_endstop(self.helper.probe_switch_site)
+        switch_zero = nozzle_zero
+        #switch_zero = self._probe_on_z_endstop(self.helper.probe_switch_site)
         # probe position on bed
         probe_zero = self._probe_on_bed(self.helper.probe_bed_site)
         # move up by retract_dist
