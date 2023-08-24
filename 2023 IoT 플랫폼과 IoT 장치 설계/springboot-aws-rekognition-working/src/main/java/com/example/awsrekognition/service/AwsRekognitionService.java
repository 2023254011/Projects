package com.example.awsrekognition.service;

import com.amazonaws.services.rekognition.AmazonRekognition;
import com.amazonaws.services.rekognition.model.*;
import org.springframework.stereotype.Service;
import org.springframework.web.multipart.MultipartFile;

import java.io.IOException;
import java.nio.ByteBuffer;

@Service
public class AwsRekognitionService {

    private AmazonRekognition client;

    public AwsRekognitionService(AmazonRekognition client) {
        this.client = client;
    }

    public AmazonRekognition returnClient() {
        return client;
    }

    public DetectModerationLabelsResult detectModerationLabels(MultipartFile imageToCheck) throws IOException {
        DetectModerationLabelsRequest request = new DetectModerationLabelsRequest()
                .withImage(new Image().withBytes(ByteBuffer.wrap(imageToCheck.getBytes())));

        return client.detectModerationLabels(request);
    }

    public DetectLabelsResult detectLabels(MultipartFile imageToCheck) throws IOException {
        DetectLabelsRequest request = new DetectLabelsRequest()
                .withImage(new Image().withBytes(ByteBuffer.wrap(imageToCheck.getBytes())));

        return client.detectLabels(request);
    }

    public DetectFacesResult detectFaces(MultipartFile imageToCheck) throws IOException {
        DetectFacesRequest request = new DetectFacesRequest()
                .withImage(new Image().withBytes(ByteBuffer.wrap(imageToCheck.getBytes())));

        return client.detectFaces(request);
    }


}
