#!/bin/bash
echo "Iniciando build mobile..."
sleep 2
echo "[INFO] Compilando APK..."
sleep 2
echo "[ERROR] Cannot resolve dependency: react-native-device-info" > build_log.txt
echo "[WARNING] Some deprecated APIs used" >> build_log.txt
echo "[INFO] Build finalizado"