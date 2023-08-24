package com.example.awsrekognition.rest;

import com.example.awsrekognition.service.AwsRekognitionService;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.multipart.MultipartFile;

import java.io.IOException;

@RestController
@RequestMapping("/api")
public class AwsRekognitionRestController {

    private AwsRekognitionService awsRekognitionService;

    public AwsRekognitionRestController(AwsRekognitionService awsRekognitionService) {
        this.awsRekognitionService = awsRekognitionService;
    }

    @PostMapping("/images/detect-moderation-labels")
    public Object detectModerationLabels(@RequestParam MultipartFile image) throws IOException {
        return ResponseEntity.ok(awsRekognitionService.detectModerationLabels(image));
    }

    @PostMapping("/images/detect-labels")
    public Object detectLabels(@RequestParam MultipartFile image) throws IOException {
        return ResponseEntity.ok(awsRekognitionService.detectLabels(image));
    }

    @PostMapping("/images/detect-faces")
    public Object detectFaces(@RequestParam MultipartFile image) throws IOException {
        return ResponseEntity.ok(awsRekognitionService.detectFaces(image));
    }




}


