package com.example.awsrekognition.controller;
/*
import com.amazonaws.services.rekognition.AmazonRekognition;
import com.amazonaws.services.rekognition.AmazonRekognitionClientBuilder;
import com.amazonaws.services.rekognition.model.*;
import com.example.awsrekognition.service.AwsRekognitionService;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

import java.util.List;

@Controller
public class FaceDetectionController {

    private AwsRekognitionService awsRekognitionService;

    public FaceDetectionController(AwsRekognitionService awsRekognitionService) {
        this.awsRekognitionService = awsRekognitionService;
    }


    @GetMapping("detectface")
    public String detectface(Model model) {
        String photo = "water_people.jpg";
        String bucket = "photo-collection2";
        String resultstring = "";

//        AmazonRekognition rekognitionClient = AmazonRekognitionClientBuilder.defaultClient();
        AmazonRekognition rekognitionClient = awsRekognitionService.returnClient();

        DetectFacesRequest request = new DetectFacesRequest()
                .withImage(new Image()
                        .withS3Object(new S3Object()
                                .withName(photo)
                                .withBucket(bucket)))
                .withAttributes(Attribute.ALL);

        try {
            DetectFacesResult result = rekognitionClient.detectFaces(request);
            List< FaceDetail > faceDetails = result.getFaceDetails();

            for (FaceDetail face: faceDetails) {
                if (request.getAttributes().contains("ALL")) {
                    AgeRange ageRange = face.getAgeRange();
                    resultstring = resultstring + "The detected face is estimated to be between " + ageRange.getLow().toString() + " and " + ageRange.getHigh().toString() + " years old.";

                    System.out.println(result);
                    System.out.println("Here's the complete set of attributes:");
                } else { // non-default attributes have null values.
                    System.out.println("Here's the default set of attributes:");
                }

                ObjectMapper objectMapper = new ObjectMapper();
                System.out.println(objectMapper.writerWithDefaultPrettyPrinter().writeValueAsString(face));
            }
            model.addAttribute("facedetectionresult", resultstring);
        } catch (AmazonRekognitionException e) {
            e.printStackTrace();
        } catch (JsonProcessingException e) {
            e.printStackTrace();
        }

        return "facedetection";

    }

}
*/